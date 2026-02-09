
import sys
import os
import traceback

# Add current directory to sys.path
sys.path.insert(0, os.getcwd())

try:
    print("Attempting to import routes.user_routes...")
    from routes.user_routes import router as user_router
    print("Successfully imported routes.user_routes")
    
    print("Attempting to import main...")
    import main
    print("Successfully imported main")
    
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
    sys.exit(1)
