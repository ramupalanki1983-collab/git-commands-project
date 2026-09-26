# Python Project – Git Workflow Demonstration

## Project Overview

This project demonstrates how to create a Python project locally, initialize it as a Git repository, track changes, create meaningful commits, review differences, use `.gitignore`, and publish the repository to GitHub.

The project contains multiple Python files demonstrating a simple learning platform.

## Project Structure

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

### student.py

Contains the `Student` class with student information and a method to display student details.

### course.py

Contains the `Course` class with course information and a method to display course details.

### utils.py

Contains reusable utility functions such as displaying headings and calculating course fees.

### main.py

The main application file. It creates Student and Course objects and demonstrates the utility functions.

---

# Git Commands Demonstrated

## 1. git init

```bash
git init
```

### Purpose

Initializes a new Git repository in the current project directory.

It creates a hidden `.git` directory where Git stores repository information, commit history, branches, and configuration.

---

## 2. git status

```bash
git status
```

### Purpose

Displays the current state of the Git repository.

It shows:

* Untracked files
* Modified files
* Staged files
* Files ready to be committed
* Current branch information

---

## 3. git add

```bash
git add student.py
```

or:

```bash
git add .
```

### Purpose

Moves changes from the working directory into the staging area.

The staging area allows us to select exactly which changes should be included in the next commit.

---

## 4. git commit

```bash
git commit -m "Add Student class"
```

### Purpose

Creates a permanent snapshot of the staged changes in the Git repository.

The `-m` option allows us to provide a meaningful commit message.

---

## 5. git log

```bash
git log
```

### Purpose

Displays the complete commit history of the repository.

A shorter version can be viewed using:

```bash
git log --oneline
```

This provides a compact list of commits.

---

## 6. git diff

```bash
git diff
```

### Purpose

Shows the differences between the current working files and the last committed version.

It is useful for reviewing changes before staging and committing them.

---

## 7. .gitignore

The `.gitignore` file contains files and folders that Git should not track.

Example:

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

This prevents unnecessary or sensitive files from being added to the repository.

---

# Complete Git Workflow

The workflow used in this project was:

```text
Create Python Project
        ↓
git init
        ↓
Create / Modify Files
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
git log
        ↓
Modify Files
        ↓
git diff
        ↓
git add
        ↓
git commit
        ↓
Create .gitignore
        ↓
git add
        ↓
git commit
        ↓
Create GitHub Repository
        ↓
Connect Local Repository to GitHub
        ↓
git push
```

# Commit History

The project contains multiple meaningful commits:

1. `Add Student class`
2. `Add Course class`
3. `Add utility functions`
4. `Add main application`
5. `Improve heading formatting`
6. `Add Git ignore configuration`

Each commit represents a meaningful stage of development.

---

# Running the Project

Make sure Python is installed.

Run:

```bash
python main.py
```

The application displays student information, course information, and the calculated course fee.

---

# Publishing the Repository to GitHub

After creating the GitHub repository, connect the local repository using:

```bash
git remote add origin https://github.com/YOUR_USERNAME/git-python-project.git
```

Rename the local branch to `main`:

```bash
git branch -M main
```

Push the project to GitHub:

```bash
git push -u origin main
```

The `-u` option establishes the upstream relationship between the local `main` branch and the GitHub `main` branch.

After this, future pushes can usually be performed using:

```bash
git push
```

---

# Verification

After pushing the project, open the GitHub repository and verify that:

* All Python files are present
* `.gitignore` is present
* `README.md` is present
* The repository is public
* The complete commit history is visible
* At least five meaningful commits are available

## Submission

Submit the public GitHub repository URL:

```text
https://github.com/YOUR_USERNAME/git-python-project
```


## Verified Commit History

The repository was developed using multiple meaningful commits.

Run the following command to view the complete commit history:

```bash
git log --oneline
