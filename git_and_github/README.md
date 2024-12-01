```bash

cp disk_usage.py disk_usage_original.py
cp disk_usage.py disk_usage_fixed.py

# make changes - fixed
# generate diff

diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diff

# patch diff file
patch disk_usage.py < disk_usage.diff

```

```bash
git config -l
git config list
```

### Guidelines for writing commit messages

A commit message is generally broken into two sections: a short summary and a description of the changes. When the git commit command is run, Git will open a text editor to write your commit message. A good commit message includes the following:

**Summary:** The first line contains the summary, formatted as a header, containing 50 characters or less.

**Description:** The description is usually kept under 72 characters and provides detailed information about the change. It can include references to bugs or issues that will be fixed with the change. It also can include links to more information when relevant.

Click the link to review an example of a commit message:

- https://commit.style/

### Terms and definitions

- **Commit:** A command to make edits to multiple files and treat that collection of edits as a single change
- **Commit files:** A stage where the changes made to files are safely stored in a snapshot in the Git directory
- **Commit message:** A summary and description with contextual information on the parts of the code or configuration of the commit change
- **Diff:** A command to find the differences between two files
- **DNS zone file:** A configuration file that specifies the mappings between IP addresses and host names in your network
- **Git:** A free open source version control system available for installation on Unix based platforms, Windows and macOS
- **Git directory:** A database for a Git project that stores the changes and the change history
- **Git log:** A log that displays commit messages
- **Git staging area:** A file maintained by Git that contains all the information about what files and changes are going to go into the next commit
- **Modified files:** A stage where changes have been made to a file, but the have not been stored or committed
- **Patch:** A command that can detect that there were changes made to the file and will do its best to apply the changes
- **Repository:** An organization system of files that contain separate software projects
- **Source Control Management (SCM):** A tool similar to VCS to store source code
- **Stage files:** A stage where the changes to files are ready to be committed
- **Tracked:** A file’s changes are recorded
- **Untracked:** A file’s changes are not recorded
- **Version control systems (VCS):** A tool to safely test code before releasing it, allow multiple people collaborate on the same coding projects together, and stores the history of that code and configuration

```bash
git log -p # patch 
git show e1f7964
git log --stat
git add -p
git diff --staged
git rm disk_usage_original.py
git mv disk_usage.py check_free_space.py
```

```bash
echo .DS_STORE > .gitignore
```

```bash
git checkout all_checks.py
git add *
git reset HEAD output.txt
```

```bash
git add gather-information.sh
git commit --amend
```

```bash
git revert HEAD
git log -p -2
```

```bash
git log --oneline
git show d6c6c89
git revert d6c6c89
```