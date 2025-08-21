import os
import sys
import subprocess
import venv
import platform
from pathlib import Path
from flask.cli import FlaskGroup   # 👈 Import para CLI
from app.app import create_app     # 👈 Usa a factory do app
from db.db import db               # 👈 Para migrações

# ========================================
# Cores para print
# ========================================
class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    NC = "\033[0m"


def print_status(message):
    print(f"{Colors.BLUE}[INFO]{Colors.NC} {message}")


def print_success(message):
    print(f"{Colors.GREEN}[SUCCESS]{Colors.NC} {message}")


def print_warning(message):
    print(f"{Colors.YELLOW}[WARNING]{Colors.NC} {message}")


def print_error(message):
    print(f"{Colors.RED}[ERROR]{Colors.NC} {message}")


def run_command(command, check=True, shell=False):
    try:
        if isinstance(command, str):
            result = subprocess.run(
                command, shell=True, check=check, capture_output=True, text=True
            )
        else:
            result = subprocess.run(
                command, shell=False, check=check, capture_output=True, text=True
            )
        return result
    except subprocess.CalledProcessError as e:
        if check:
            print_error(f"Command failed: {command}")
            print_error(f"Error: {e.stderr}")
            sys.exit(1)
        return e


# ========================================
# Setup helpers
# ========================================
def check_python_version():
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error("Python 3.8 or higher is required")
        sys.exit(1)
    print_status(f"Python version: {version.major}.{version.minor}.{version.micro}")


def create_virtual_environment():
    venv_path = Path("venv")
    if not venv_path.exists():
        print_status("Creating virtual environment...")
        venv.create("venv", with_pip=True)
        print_success("Virtual environment created successfully!")
    else:
        print_status("Virtual environment already exists.")


def get_python_executable():
    if platform.system() == "Windows":
        return os.path.abspath("venv\\Scripts\\python.exe")
    else:
        return os.path.abspath("venv/bin/python")


def get_pip_executable():
    if platform.system() == "Windows":
        return os.path.abspath("venv\\Scripts\\pip.exe")
    else:
        return os.path.abspath("venv/bin/pip")


def install_requirements():
    pip_exec = get_pip_executable()

    print_status("Upgrading pip...")
    run_command([pip_exec, "install", "--upgrade", "pip"])

    print_status("Installing requirements...")
    if Path("requirements.txt").exists():
        run_command([pip_exec, "install", "-r", "requirements.txt"])
        print_success("Requirements installed successfully!")
    else:
        print_error("requirements.txt not found!")
        sys.exit(1)


def create_env_template():
    env_path = Path(".env")
    if not env_path.exists():
        print_warning(".env file not found. Creating template...")
        env_content = "DATABASE_URL=postgresql://user:password@localhost:5432/dbname\n"
        with open(".env", "w") as f:
            f.write(env_content)
        print_warning("Please edit .env file with your actual database credentials!")
    else:
        print_status("Reading existing .env file...")
        with open(".env", "r") as f:
            env_content = f.read()
        print_success("Environment variables loaded from .env file")


def check_project_structure():
    if not Path("app").exists():
        print_error("app directory not found!")
        sys.exit(1)

    if not Path("app/app.py").exists():
        print_error("app/app.py not found!")
        sys.exit(1)


def run_flask_app():
    python_exec = get_python_executable()
    print_success("Setup completed successfully!")
    print("")
    print_status("Starting Flask application...")
    print("")
    os.chdir("app")
    subprocess.run([python_exec, "app.py"])


# ========================================
# CLI do Flask (migrações, etc)
# ========================================
app = create_app()
cli = FlaskGroup(app)

# ========================================
# Entry point
# ========================================
def main():
    print("🚀 Starting Big Bear's Cave Backend Setup...")
    print("")

    check_python_version()
    create_virtual_environment()
    install_requirements()
    create_env_template()
    check_project_structure()
    run_flask_app()


if __name__ == "__main__":
    # Se rodar com: python run.py -> roda setup normal
    # Se rodar com: flask db migrate/upgrade -> funciona CLI
    if len(sys.argv) > 1:
        cli()   # 👈 executa comandos do flask (db migrate, db upgrade, etc)
    else:
        main()
