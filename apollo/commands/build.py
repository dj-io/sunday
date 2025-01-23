from apollo.utils.run_command import run_command
from apollo.utils.config import load_config, cache_apollo_path
from halo import Halo
import os
import subprocess
import click

@click.option("--lint-skip", is_flag=True, help="Build without linting checks")
def build(lint_skip):
    
    config = load_config()

    # ensure apollo path has been set
    cache_apollo_path(config)
    
    # run pwd from project dir to update path
    APOLLO_PATH = config["apollo_path"]
    
    # run pwd from project dir to update path in .config file 
    REQUIREMENTS_FILE = os.path.join(APOLLO_PATH, "requirements.txt")
    
    spinner = Halo(spinner="dots")

    if os.path.exists(REQUIREMENTS_FILE):
        try:
            run_command(f"pip3 install -r {REQUIREMENTS_FILE}", APOLLO_PATH, start="Checking for dependencies...")
            spinner.succeed("requirements.txt found. Installing dependencies...")
        except subprocess.CalledProcessError as e:
            spinner.fail(f"Failed to install dependencies: {e.stderr}")
            return
        
        # Step 2: Verify code quality and run tests
    try:
        if not lint_skip:
            run_command("flake8 .", APOLLO_PATH, start="Checking code quality...")
            spinner.succeed("Code quality checks passed.")

        run_command("pytest --maxfail=1 --disable-warnings", APOLLO_PATH, start="Running tests...")
        spinner.succeed("All tests passed.")
    except subprocess.CalledProcessError as e:        
        spinner.fail("Build failed due to code quality or test failures.")
        print("Errors/Stack Trace:")
        
        if e.stdout or e.stderr:
            spinner.fail("\n".join(output.strip() for output in [e.stdout, e.stderr] if output))
            
        spinner.info("Please resolve the issues above and try again.")
        exit(1)

        
    """Clean and rebuild the package (developer only)."""
    while True:
        try:
            run_command("rm -rf dist/ build/ *.egg-info", APOLLO_PATH, start="Cleaning up old build artifacts...")
            spinner.succeed("Old build artifacts cleaned up.")
            
            run_command("python3 -m build", APOLLO_PATH, start="Building the package...")
            spinner.succeed("Package built successfully.")
            
            run_command("pip3 install dist/*.whl --force-reinstall", APOLLO_PATH, start="Installing locally for testing...")
            spinner.succeed("Package installed locally for testing.")
            
            spinner.succeed("Build completed successfully! 🎉")
            spinner.info("Ok to Test your local changes...")
            break
        except subprocess.CalledProcessError as e:
            spinner.fail(f"Build failed with error: {e.stderr}")
            retry = input("Would you like to fix the issue and retry? (yes/no): ").strip().lower()
            if retry == "yes":
                spinner.start("Waiting for fixes... Please resolve the issues before retrying.")
                spinner.stop()
            else:
                spinner.fail("Exiting build process.")
                break
                
        
