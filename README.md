# Python Project – Git & GitHub Workflow Demonstration

## Project Overview

This project demonstrates a complete Git workflow using a Python project.

The project was created locally, initialized with Git, developed using multiple Python files, committed in meaningful stages, and finally published to a public GitHub repository.

The following Git concepts and commands are demonstrated:

- `git init`
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`
- `.gitignore`
- `git remote`
- `git branch`
- `git push`

The repository contains **multiple meaningful commits** so that the complete development history can be reviewed on GitHub.

---

# Project Structure

```text
git-python-project/
│
├── main.py
├── student.py
├── course.py
├── utils.py
├── .gitignore
└── README.md
```

## Python Files

### `student.py`

Contains the `Student` class.

The class stores:

- Student ID
- Student name
- Course

It also contains a method to display student information.

### `course.py`

Contains the `Course` class.

The class stores:

- Course ID
- Course name
- Instructor

It also contains a method to display course information.

### `utils.py`

Contains reusable utility functions.

The project uses utility functions for:

- Displaying headings
- Calculating course fees after applying a discount

### `main.py`

The main application file.

It imports the Student, Course, and utility classes/functions and demonstrates how they work together.

---

# Running the Python Project

Make sure Python is installed.

Run:

```bash
python main.py
```

Example output:

```text
========================================
Python Learning Platform
========================================

ID: 101, Name: Ramu, Course: Python Programming
Course ID: PY101, Course: Python Programming, Instructor: John
Course Fee after discount: ₹9000.00
```

---

# Git Workflow

The project was developed using the following workflow:

```text
Create Python Project
        ↓
git init
        ↓
git status
        ↓
Create Python Files
        ↓
git add
        ↓
git commit
        ↓
Modify Project
        ↓
git diff
        ↓
git add
        ↓
git commit
        ↓
Create .gitignore
        ↓
git commit
        ↓
Create README.md
        ↓
git commit
        ↓
git log
        ↓
Connect Local Repository to GitHub
        ↓
git push
        ↓
Verify Commit History on GitHub
```

---

# Git Commands Demonstrated

## 1. git init

```bash
git init
```

### Purpose

`git init` initializes the current directory as a Git repository.

It creates a hidden `.git` directory that stores Git's internal information, including:

- Commit history
- Branch information
- Repository configuration
- Staging information

This command was the first Git command used in the project.

---

# 2. git status

```bash
git status
```

### Purpose

`git status` displays the current state of the Git repository.

It can show:

- Untracked files
- Modified files
- Staged files
- Files ready for commit
- Current branch
- Whether the working tree is clean

### Demonstration

After modifying a file, the following command was executed:

```bash
git status
```

### Actual Output

> Replace the text below with the actual output from your terminal.

```text
PASTE YOUR ACTUAL git status OUTPUT HERE
```

### What this demonstrates

The output shows which files have been modified or are waiting to be staged.

---

# 3. git add

```bash
git add student.py
```

or:

```bash
git add .
```

### Purpose

`git add` moves changes from the working directory to the staging area.

The staging area allows us to select the changes that should be included in the next commit.

Example:

```bash
git add student.py
```

Stages only `student.py`.

Example:

```bash
git add .
```

Stages all eligible changes in the current directory.

---

# 4. git commit

```bash
git commit -m "Add Student class"
```

### Purpose

`git commit` creates a permanent snapshot of the changes that have been staged.

The `-m` option allows us to provide a meaningful description of the changes.

Examples of meaningful commits used in this project:

```text
Add Student class
Add Course class
Add utility functions
Add main application
Improve heading formatting
Add Git ignore configuration
Add project documentation
```

Each commit represents a meaningful stage of development.

---

# 5. git log

```bash
git log
```

### Purpose

`git log` displays the commit history of the repository.

A compact version can be displayed using:

```bash
git log --oneline
```

### Demonstration

The following command was executed after completing the development:

```bash
git log --oneline
```

### Actual Output

> Replace the text below with the actual output from your terminal.

```text
PASTE YOUR ACTUAL git log --oneline OUTPUT HERE
```

### What this demonstrates

The output provides evidence that the project contains multiple meaningful commits and shows the chronological development history.

---

# 6. git diff

```bash
git diff
```

### Purpose

`git diff` displays changes that have been made to tracked files but have not yet been staged.

It is useful for reviewing changes before running `git add`.

### Demonstration

A change was made to `utils.py` before staging the file.

The following command was then executed:

```bash
git diff
```

### Actual Output

> Replace the text below with the actual output from your terminal.

```text
PASTE YOUR ACTUAL git diff OUTPUT HERE
```

### What this demonstrates

The output shows the exact lines that were added, removed, or changed since the previous commit.

---

# 7. .gitignore

The `.gitignore` file tells Git which files and directories should not be tracked.

The project uses:

```gitignore
__pycache__/
*.pyc
.env
.venv/
venv/
.vscode/
.idea/
*.log
```

### Why `.gitignore` is required

Some files should not be stored in Git, such as:

- Python cache files
- Compiled Python files
- Virtual environments
- Environment configuration files
- IDE-specific settings
- Log files

For example, `.env` files may contain sensitive configuration values and should generally not be committed.

---

# 8. git remote

```bash
git remote add origin https://github.com/YOUR_USERNAME/git-python-project.git
```

### Purpose

`git remote` connects the local Git repository to a remote repository.

Here:

- `origin` is the name given to the remote repository.
- The GitHub URL identifies the remote repository.

The remote can be verified using:

```bash
git remote -v
```

Example:

```text
origin  https://github.com/YOUR_USERNAME/git-python-project.git (fetch)
origin  https://github.com/YOUR_USERNAME/git-python-project.git (push)
```

---

# 9. git branch

```bash
git branch -M main
```

### Purpose

This command renames the current branch to `main`.

The `main` branch is commonly used as the primary branch of a GitHub repository.

The current branch can be checked using:

```bash
git branch
```

Expected result:

```text
* main
```

---

# 10. git push

```bash
git push -u origin main
```

### Purpose

`git push` uploads local commits to the remote GitHub repository.

The `-u` option establishes the upstream relationship between the local `main` branch and the remote `main` branch.

After the upstream relationship is established, future pushes can normally be performed using:

```bash
git push
```

---

# Complete Git Command Sequence

The following commands represent the overall workflow used for this project:

```bash
mkdir git-python-project
cd git-python-project

git init

git status

git add student.py
git commit -m "Add Student class"

git add course.py
git commit -m "Add Course class"

git add utils.py
git commit -m "Add utility functions"

git add main.py
git commit -m "Add main application"

git diff

git add utils.py
git commit -m "Improve heading formatting"

git add .gitignore
git commit -m "Add Git ignore configuration"

git add README.md
git commit -m "Add project documentation"

git log --oneline

git remote add origin https://github.com/YOUR_USERNAME/git-python-project.git

git branch -M main

git push -u origin main
```

---

# Meaningful Commit History

The project was intentionally developed through multiple meaningful commits instead of creating one large commit at the end.

The intended commit sequence is:

1. `Add Student class`
2. `Add Course class`
3. `Add utility functions`
4. `Add main application`
5. `Improve heading formatting`
6. `Add Git ignore configuration`
7. `Add project documentation`

## Actual Commit History

The actual Git history should be verified using:

```bash
git log --oneline
```

Paste the actual output below:

```text
PASTE YOUR ACTUAL git log --oneline OUTPUT HERE
```

The commit history can also be verified from the **Commits** section of the GitHub repository.

---

# Final Git Status

After all changes have been committed, run:

```bash
git status
```

### Actual Output

> Replace the text below with your actual final output.

```text
PASTE YOUR ACTUAL FINAL git status OUTPUT HERE
```

A clean repository normally displays:

```text
nothing to commit, working tree clean
```

This confirms that there are no uncommitted changes remaining.

---

# GitHub Repository

The local repository was published to GitHub using:

```bash
git push -u origin main
```

Public GitHub repository:

```text
https://github.com/YOUR_USERNAME/git-python-project
```

Replace `YOUR_USERNAME` with the actual GitHub username.

---

# GitHub Verification

After pushing the repository, verify the following on GitHub:

- [ ] Repository is public
- [ ] `main.py` is present
- [ ] `student.py` is present
- [ ] `course.py` is present
- [ ] `utils.py` is present
- [ ] `.gitignore` is present
- [ ] `README.md` is present
- [ ] Multiple meaningful commits are visible
- [ ] Complete commit history is available
- [ ] The latest commit has been pushed successfully

The GitHub **Commits** page provides the final verification of the project's commit history.

---

# Evidence / Screenshots

The following evidence was captured during the Git workflow:

## 1. git init

Screenshot showing the repository being initialized:

```text
[INSERT SCREENSHOT HERE]
```

## 2. git status

Screenshot showing repository status:

```text
[INSERT SCREENSHOT HERE]
```

## 3. git diff

Screenshot showing changes before staging:

```text
[INSERT SCREENSHOT HERE]
```

## 4. git log

Screenshot showing the complete commit history:

```text
[INSERT SCREENSHOT HERE]
```

## 5. Final git status

Screenshot showing the clean working tree:

```text
[INSERT SCREENSHOT HERE]
```

## 6. GitHub Commit History

Screenshot showing the commits on the public GitHub repository:

```text
[INSERT SCREENSHOT HERE]
```

---

# Learning Outcomes

After completing this project, the following Git and GitHub concepts are demonstrated:

- Creating a local Git repository
- Understanding the working directory
- Understanding the staging area
- Tracking files with Git
- Creating meaningful commits
- Reviewing changes with `git diff`
- Viewing commit history with `git log`
- Ignoring files using `.gitignore`
- Connecting a local repository to GitHub
- Working with the `main` branch
- Pushing local commits to GitHub
- Verifying commit history on GitHub
- Following a complete local-to-remote Git workflow

---

# Assignment Requirements Checklist

| Requirement | Status |
|---|---|
| Create Python project locally | Completed |
| Initialize using `git init` | Completed |
| Add at least 4 Python files | Completed |
| Demonstrate `git status` | Completed |
| Demonstrate `git add` | Completed |
| Demonstrate `git commit` | Completed |
| Demonstrate `git log` | Completed |
| Demonstrate `git diff` | Completed |
| Demonstrate `.gitignore` | Completed |
| Make at least 5 meaningful commits | Completed |
| Publish repository on GitHub | Completed |
| Create README explaining Git commands | Completed |
| Document actual command output | Add actual terminal output |
| Provide GitHub repository URL | Add actual URL |
| Verify complete commit history on GitHub | Completed |

---

# Submission

Submit the public GitHub repository URL:

```text
https://github.com/YOUR_USERNAME/git-python-project
```

The repository should contain the complete Python project, README documentation, `.gitignore`, and the complete Git commit history.
