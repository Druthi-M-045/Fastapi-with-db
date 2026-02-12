import urllib.request
import urllib.parse
import json
import time

BASE_URL = "http://localhost:8000"
USER_EMAIL = "testuser_history@example.com"
USER_PASSWORD = "testpassword123"

def make_request(url, method="GET", data=None, headers=None):
    if headers is None:
        headers = {}
    
    req = urllib.request.Request(url, method=method)
    for k, v in headers.items():
        req.add_header(k, v)
    
    if data:
        json_data = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
        req.data = json_data

    try:
        with urllib.request.urlopen(req) as response:
            status = response.status
            body = response.read().decode("utf-8")
            try:
                json_body = json.loads(body)
            except:
                json_body = body
            return status, json_body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return e.code, body
    except Exception as e:
        return 0, str(e)

def print_result(step, success, message=""):
    status = "SUCCESS" if success else "FAILURE"
    print(f"[{status}] {step}: {message}")

def verify_history():
    print("Starting verification of history implementation...")
    
    # 1. Signup
    print("Attempting signup...")
    status, response = make_request(
        f"{BASE_URL}/signup", 
        method="POST", 
        data={"email": USER_EMAIL, "password": USER_PASSWORD}
    )
    
    if status == 200:
        print_result("Signup", True, "User created successfully")
    elif status == 400 and "User already exists" in str(response):
        print_result("Signup", True, "User already exists (expected)")
    else:
        print_result("Signup", False, f"Unexpected status code: {status}, {response}")
        return

    # 2. Login
    print("Attempting login...")
    status, response = make_request(
        f"{BASE_URL}/login", 
        method="POST", 
        data={"email": USER_EMAIL, "password": USER_PASSWORD}
    )
    
    if status == 200:
        access_token = response.get("access_token")
        print_result("Login", True, "Logged in successfully")
    else:
        print_result("Login", False, f"Failed to login: {status}, {response}")
        return

    headers = {"Authorization": f"Bearer {access_token}"}

    # 3. Ask AI
    question = "Hello, testing history!"
    print(f"Asking AI: {question}")
    status, response = make_request(
        f"{BASE_URL}/ask", 
        method="POST", 
        data={"message": question}, 
        headers=headers
    )
    
    if status == 200:
        ai_response = response.get("response")
        print_result("Ask AI", True, f"AI Responded: {ai_response}")
    else:
        print_result("Ask AI", False, f"Failed to get AI response: {status}, {response}")
        return

    time.sleep(1)

    # 4. Get History
    print("Retrieving history...")
    status, response = make_request(
        f"{BASE_URL}/history", 
        method="GET", 
        headers=headers
    )
    
    if status == 200:
        history = response
        found = False
        for entry in history:
            if entry.get("input_text") == question:
                found = True
                print_result("Get History", True, f"Found history entry: {entry}")
                break
        
        if not found:
            print_result("Get History", False, f"History entry not found for question: {question}. Only found: {history}")
    else:
        print_result("Get History", False, f"Failed to get history: {status}, {response}")

if __name__ == "__main__":
    verify_history()
