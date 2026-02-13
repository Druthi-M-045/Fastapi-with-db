
import sys
import os
import schemas

print(f"Current Working Directory: {os.getcwd()}")
print(f"sys.path: {sys.path}")
print(f"schemas.__file__: {getattr(schemas, '__file__', 'No __file__')}")
print(f"schemas.__path__: {getattr(schemas, '__path__', 'No __path__')}")

for schema_name in ["User_schemas", "History_schemas", "Token_schemas", "ai_response_schemas"]:
    try:
        exec(f"from schemas import {schema_name}")
        print(f"from schemas import {schema_name}: SUCCESS")
    except ImportError as e:
        print(f"from schemas import {schema_name}: FAILED ({e})")

try:
    from routes.user_routes import router
    print("from routes.user_routes import router: SUCCESS")
except ImportError as e:
    print(f"from routes.user_routes import router: FAILED ({e})")
