
import sys
import os
import traceback

sys.path.insert(0, os.getcwd())

try:
    print("Attempting to import main...")
    import main
    print("Successfully imported main")
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
    sys.exit(1)
