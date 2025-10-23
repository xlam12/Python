#!/usr/bin/env python3
"""
hello_devops.py — A simple DevOps-friendly CLI that prints system information.
"""

import os
import sys
import platform
import subprocess


def main() -> None:
    print("=" * 40)
    print("👋 Hello DevOps!")
    print("=" * 40)

    print(f"User: {os.getenv('USER') or os.getenv('USERNAME')}")
    print(f"Hostname: {platform.node()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Python Executable: {sys.executable}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Total Installed Modules: {len(sys.modules)}")
    print(f"Example Env Var (PATH): {os.getenv('PATH')}")
    print("=" * 40)


if __name__ == "__main__":
    main()
