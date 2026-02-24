"""
Backend startup script
Run from project root: python run_backend.py
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
os.environ['PYTHONPATH'] = project_root

# Import and run
import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("Starting EmpowerWork Backend Server")
    print("=" * 60)
    print("Server will run on: http://localhost:8000")
    print("API Docs: http://localhost:8000/docs")
    print("Press CTRL+C to stop")
    print("=" * 60)
    print()
    
    uvicorn.run(
        "backend.src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

