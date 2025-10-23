
import os


def main():
    print("Hello DevOps!")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Environment Variables: {os.environ}")
    print(f"Python Version: {os.sys.version}")
    print(f"Python Executable: {os.sys.executable}")
    print(f"Installed Packages: {os.sys.modules.keys()}")
    print(f"sys.path: {os.sys.path}")
    print(f"os.platform = {os.uname().sysname}")


if __name__ == "__main__":
    main()



