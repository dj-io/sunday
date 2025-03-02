
 <h1 align="center"> Sunday CLI 🌔 </h1>

<p align="center">
  <a href="https://pypi.org/project/sunday-cli/0.1.0/">
    <img src="https://img.shields.io/pypi/v/sunday-cli.svg" alt="PyPI Version">
  </a>
  <a href="https://github.com/dj-io/sunday/blob/main/sunday-cli/LICENSE">
    <img src="https://img.shields.io/github/license/dj-io/sunday.svg" alt="License">
  </a>
  <a href="https://github.com/dj-io/sunday-cli/actions">
    <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Build Status">
  </a>
  <!-- <a href="https://coveralls.io/github/psf/sunday?branch=main"> -->
    <img src="https://img.shields.io/badge/coverage-36%25-brightgreen" alt="Coverage Status">
  <!-- </a> -->
  </a>
    <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style">
  </a>
</p>

Sunday CLI is an, AI Powered, command-line interface designed to streamline the SDLC by automating project workflows. Includes automations for source control, CI/CD, ticket and documentation generation, and other processes. 

This tool simplifies tasks like managing source control repositories i.e Github, CI/CD i.e github actions, Project management workflows and more, allowing teams to focus on building and delivering software efficiently.

# Table of Contents

- [Features ⚙️](#-features-⚙️)
- [Getting Started 🔑](#getting-started-🔑)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage 🛠](#usage-🛠️) ️
  - [Show Available Commands](#show-available-commands)
  - [Show Command Features: `sun <command> --help`](#show-command-features)
    - [Usage](#usage-1)
    - [Key Features](#key-features)
- [Contributing 💡](#contributing-💡)
  - [Developer Mode 🪄](#developer-mode-🪄)
    - [Setting Up Developer Mode](#setting-up-developer-mode)
    - [Using Developer Mode](#using-developer-mode)
  - [Guidelines](#guidelines)
  - [Versioning](#versioning)
- [License 📜](#license-📜 )  
- [Acknowledgments 🙏](#acknowledgments-🙏) 

# ️ Features ⚙️ 

 - **Automation Tools**: Scripts for automating repetitive tasks, such as data processing, file management, github actions, and API integration.
- **Data Utilities**: Scripts for data extraction, transformation, and analysis, including  
basic visualizations.
 - **Task Scheduling**: Scripts to schedule and automate recurring tasks (e.g., backups, log parsing).

 # Getting Started 🔑
 
 ### Prerequisites

Ensure you have the following installed:

- **Python3** for running the scripts in this repo
- **Pip3** pythons package manager used to install the pypi package sunday 

## Installation

### Via [PyPI](https://pypi.org/project/sunday-cli/0.1.0/)

Install the latest version using `pip`:

```bash
pip install sunday
```

### Via Source

Clone the repository and install it locally:
```bash
git clone https://github.com/dj-io/sunday/sunday-cli.git
cd sunday-cli
pip install -r requirements.txt
```

## Usage 🛠

Sunday provides a collection of commands designed to streamline your development workflows. After installation, the sun command is available in your terminal.

### Show Available Commands

Run the following to see a list of available commands and their descriptions:
```bash
sun --help
```

example output:
```bash
Usage: sun [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  gh-create  Create and push a new repository to GitHub.
  gh-delete  Delete remote and local repositories, 1 by 1 or in bulk.
  gh-add     Push an existing local repository to a new GitHub repo.
```


### Show Command Features

Run the following to see a more descriptive output of commands features and usage:

```bash
sun <command> --help
```

example output:
```bash
Usage: sun gh-create [OPTIONS]

  Create a new GitHub repository and initialize it locally.

  Features:
      - Allows you to specify a repository name and description.
      - Option to choose whether the repository is public or private.
      - Automatically initializes the repository with a README.
      - Sets up a remote connection to GitHub using the GitHub CLI.


  Considerations:
      - Ensure you are authenticated with the GitHub CLI (`gh auth login`) before using this command.
      - Requires the GitHub CLI installed locally.

Options:
  -h, --help  Show this message and exit.
```

### Key Features

1. **Interactive Directory Selection**

    Sunday automatically detects directories and provides multiple options:

    - Use the current working directory.
    - Select an existing directory from a list.
    - Create a new directory if needed.

    **Example Prompt**:
    ```bash
    Would you like to use the current directory as the parent directory? (yes/no)
    ```

2. **Caching**

    The CLI stores information and preferences needed for use with various integrations i.e GitHub username for future use, eliminating repetitive inputs. If the username is already cached, the CLI will prompt you to reuse it.

    **Example Prompt**:
      ```bash
      Using cached GitHub username: dj-io
      ```


# Contributing 💡

### Getting started:

1. Fork the repository.
    ```bash
    gh repo fork https://github.com/dj-io/sunday.git --remote=true
    ```

2. Create a new branch to your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. Commit your changes:
    ```bash
    git commit -m "Description of your changes"
    ```

4. Push to your branch:
    ```bash
    git push origin feature/your-feature-name
    ```

5. Open a pull request on Github.

### Developer Mode 🪄: 

### Setting up developer mode
 
 `Developer mode enables additional CLI commands (e.g., sun build and sun deploy) that are not available in production. Follow these steps to configure and use developer mode:`

---

**1. Create Environment Files**

  - Navigate to the root directory of the project.
  - Create .env.dev and .env.prod files based on the provided .env.sample file.
  
  ```bash
  cp .env.sample .env.dev
  cp .env.sample .env.prod
  ```
- Edit the .env.dev and .env.prod files with your environment-specific variables. For example:

```bash
SUN_DEV_MODE=1
```

**2. Enable Developer Mode.**
Run the following command in your terminal to enable developer mode:

  ```bash
  export ENV=dev
  ```

- This sets the ENV variable to dev for the current terminal session, which ensures the script loads .env.dev and enables developer-specific features.

### Using Developer Mode

Developer mode commands are available for contributors to streamline package development, testing, and deployment. These commands allow developers to rebuild and deploy sunday.

---

**Available Commands**


1. **Build**
    
     Use the sunday build command to rebuild the package during development. This ensures all changes to the codebase are reflected in the package.

    ```bash
    sun build
    ```
    - **The command includes prompts to**:
      - Cleans up old build artifacts.
      - Rebuilds the package into the dist/ directory
      - Installs the package locally for testing
      - Automatically installs missing dependencies from `requirements.txt`

2. **Deploy**
    Use the sunday deploy command to package and deploy the CLI to PyPI (or TestPyPI)

    ```bash
    sun deploy
    ```
    -	The command includes prompts to:
        -	Select between TestPyPI or Prod PyPI.
        - Provide changelog or release notes.
        -	Confirm the deployment target.
        - Automatically detects the .pypirc file and verifies its validity.

    - Example

      ```bash
      sun deploy --test  # Deploy to TestPyPI
      sun deploy --prod  # Deploy to Prod PyPI
      ```

3. **Clean up**
    Use the sunday clean-up command to run linting checks and automatically resolve using `flake8` and `black`

    ```bash
    sun clean-up
    ```
    -	The command includes prompts to:
        -	Confirm clean-up action if linting issues are found.
        - Traverses code base and runs black on each file with linting issues present

**Additional Notes**

  
  - `The deploy command is only executable with credentials provided upon request`
  - **Switching Modes**:
    - To switch back to production mode, run:
    ```bash
    export ENV=prod
    ```
    - This switch happens automatically during deployments.

  - **Ensuring a Valid** `.pypirc` **File Exists**:

    The deploy command relies on the `.pypirc` configuration file for TestPyPI and ProdPyPI deployments:

    **- Automatic Detection**
    - The CLI **automatically** detects the `.pypirc` file in your home directory **(~/.pypirc)** during deployment.

    - If the file is missing or lacks the necessary credentials for TestPyPI or ProdPyPI, the CLI will prompt you to create or update it.

    **- Structure of** .pypirc:

    Ensure your .pypirc file contains the correct repository configuration:
      ```ini
      [distutils]
      index-servers =
          pypi
          testpypi

      [pypi]
      repository = https://upload.pypi.org/legacy/
      username = __token__
      password = your-prod-token

      [testpypi]
      repository = https://test.pypi.org/legacy/
      username = __token__
      password = your-test-token
      ```

    **- Prompts for Missing Credentials**:

    - **DON'T WORRY**,	If the `.pypirc` file is incomplete (e.g., missing a repository, username, or password), the CLI will guide you through updating it!
  
  - Run `sun --help` in developer mode to view the full list of available commands
  -  If you modify .env.dev or .env.prod, reload your environment variables:
      ```bash
      source ~/.zshrc  # For Zsh
      source ~/.bashrc  # For Bash
      ```


### Guidelines:

- Ensure your code is well-documented and adheres to **PEP 8** standards.
- Add **tests** for any new features or bug fixes.
- **Do Not Commit Sensitive Data**: Ensure .env.dev and .env.prod are excluded from version control by including them in .gitignore.
- **Testing Locally**: Use `sun build` to test changes locally before deploying to PyPI or TestPyPI.
- **Deploy Responsibly**: Always verify the environment (dev or prod) before running deployment commands to avoid accidental production deployments.

### Versioning:
Given a version number `major.minor.patch`, all: 

  - Breaking backwards compatibility bumps the MAJOR
  - New additions without breaking backwards compatibility bumps the MINOR
  - Bug fixes and misc changes bump the PATCH
  
  **For more information on semantic versioning, please visit http://semver.org/.**


### License: 📜
Copyright Stratum Labs LLC.

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments 🙏

`Sunday` is inspired by the need to streamline development workflows. Special thanks to all future contributors who will help shape this project.

<!-- ### Technologies Used 📚

- `Python`: For functonality and logic processing
- `Questionary`: For interactive CLI prompts.
- `OS`: For file system operations.
- `Subprocess`: For running Git commands. -->