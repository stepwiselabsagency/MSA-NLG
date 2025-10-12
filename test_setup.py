#!/usr/bin/env python3
"""
Test script to verify the application setup
"""

import os
import sys
import subprocess
import requests
import time

def check_file_exists(filepath, description):
    """Check if a file exists and print status"""
    if os.path.exists(filepath):
        print(f"[OK] {description}: {filepath}")
        return True
    else:
        print(f"[FAIL] {description}: {filepath} - NOT FOUND")
        return False

def check_directory_structure():
    """Check if all required directories and files exist"""
    print("Checking project structure...")
    
    required_files = [
        ("docker-compose.yml", "Docker Compose file"),
        ("backend/main.py", "FastAPI main file"),
        ("backend/requirements.txt", "Backend requirements"),
        ("backend/Dockerfile", "Backend Dockerfile"),
        ("frontend/package.json", "Frontend package.json"),
        ("frontend/Dockerfile", "Frontend Dockerfile"),
        ("frontend/nginx.conf", "Nginx configuration"),
        ("frontend/src/App.js", "React App component"),
        ("README.md", "README file"),
        (".gitignore", "Git ignore file")
    ]
    
    all_good = True
    for filepath, description in required_files:
        if not check_file_exists(filepath, description):
            all_good = False
    
    return all_good

def check_docker_available():
    """Check if Docker is available"""
    print("\nChecking Docker availability...")
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] Docker is available: {result.stdout.strip()}")
            return True
        else:
            print("[FAIL] Docker is not available")
            return False
    except FileNotFoundError:
        print("[FAIL] Docker is not installed")
        return False

def check_docker_compose_available():
    """Check if Docker Compose is available"""
    print("\nChecking Docker Compose availability...")
    try:
        result = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] Docker Compose is available: {result.stdout.strip()}")
            return True
        else:
            print("[FAIL] Docker Compose is not available")
            return False
    except FileNotFoundError:
        print("[FAIL] Docker Compose is not installed")
        return False

def main():
    """Main test function"""
    print("Sports Analysis Application - Setup Test")
    print("=" * 50)
    
    # Check project structure
    structure_ok = check_directory_structure()
    
    # Check Docker availability
    docker_ok = check_docker_available()
    compose_ok = check_docker_compose_available()
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    print(f"Project Structure: {'[OK] PASS' if structure_ok else '[FAIL] FAIL'}")
    print(f"Docker: {'[OK] PASS' if docker_ok else '[FAIL] FAIL'}")
    print(f"Docker Compose: {'[OK] PASS' if compose_ok else '[FAIL] FAIL'}")
    
    if structure_ok and docker_ok and compose_ok:
        print("\n[SUCCESS] All checks passed! The application is ready to run.")
        print("\nTo start the application:")
        print("  docker-compose up --build")
        print("\nAccess points:")
        print("  - Frontend: http://localhost:3000")
        print("  - Backend API: http://localhost:8000")
        print("  - API Docs: http://localhost:8000/docs")
        return 0
    else:
        print("\n[ERROR] Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
