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

```bash
git branch
git branch new-feature
git checkout new-feature
git branch
git checkout -b 'even-better-feature'
```

It will cache credentials for 15 minutes

```bash
git config --global credential.helper cache
```

```bash
git remote -v
git remote show origin
git branch -r
git status
```

```bash
git fetch
git log origin/main
git status
git merge origin/main
```

```bash
git pull
git remote show origin
git checkout exprimental
```

### Terms and definitions

- **Branch:** A pointer to a particular commit, representing an independent line of development in a project
- **Commit ID:** An identifier next to the word commit in the log
- **Fast-forward merge:** A merge when all the commits in the checked out branch are also in the branch that's being merged
- **Head:** This points to the top of the branch that is being used
- **Master:** The default branch that Git creates for when a new repository initialized, commonly used to place the approved pieces of a project
- **Merge conflict:** This occurs when the changes are made on the same part of the same file, and Git won't know how to merge those changes
- **Rollback:** The act of reverting changes made to software to a previous state
- **Three-way merge:** A merge when the snapshots at the two branch tips with the most recent common ancestor, the commit before the divergence

### Secure Shell and & API Keys

- [SSH Protocol – Secure Remote Login and File Transfer](https://www.coursera.org/learn/introduction-git-github/supplement/cecyq/the-ssh-protocol)
- [Public Key and Private Key: How they Pair & Work Together](https://www.preveil.com/blog/public-and-private-key/)
- [A Deep Dive on End-to-End Encryption](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work)
- [Difference between SFTP and SCP](https://www.tutorialspoint.com/difference-between-sftp-and-scp)
- [SSH Port Forwarding (SSH Tunneling) Explained](https://phoenixnap.com/kb/ssh-port-forwarding)
- [How to Set Up an SSH Jump Server](https://goteleport.com/blog/ssh-jump-server/)
- [Use X forwarding on a personal computer](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023566)
- [Adding your SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)
- [How To Tune your SSH Daemon Configuration on a Linux VPS](https://www.digitalocean.com/community/tutorials/how-to-tune-your-ssh-daemon-configuration-on-a-linux-vps)
- [PuTTY: a free SSH and Telnet client](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

```bash
git push -u origin refactor
git checkout main
git pull
git log --graph --oneline --all
git checkout refactor
git rebase main
git log --graph --oneline --all
git checkout main
git merge refactor
git push --delete origin refactor
git branch -d refactor
git push
```

### Terms and definitions

- **Application Programming Interface (API) key:** This is an authentication token that calls an API, which is then called to identify the person, programmer, or program trying to access a website
- **Computer protocols:** Guidelines published as open standards so that any given protocol can be implemented in various products
- **Distributed:** Each developer has a copy of the whole repository on their local machine
- **GitHub:** A web-based Git repository hosting service, allowing users to share and access repositories on the web and copy or clone them to a local computer
- **Merge:** An operation that merges the origin/master branch into a local master branch
- **Private key:** A secret and secure cryptographic key that must be kept confidential and protected and is used to decrypt data that has been encrypted with the corresponding public key
- **Public key:** A safety cryptographic structure frequently employed to establish secure communication through data encryption or to validate the authenticity of a digital signature
- **Rebasing:** The base commit that's used for a branch is changed
- **Remote branches:** Git uses read-only branches to keep copies of the data that's stored in the remote repository
- **Remote repositories:** Repositories that allow developers to contribute to a project from their own workstations making changes to local copies of the project independently of one another
- **Secure Shell (SSH):** A robust protocol for connecting to servers remotely
- **SSH client:** This establishes a connection to the SSH server, ensuring a secure interaction, where the client makes access requests
- **SSH key:** An access credential
- **SSH protocol:** Standard commonly used for logging in to servers remotely on the principle of public-key encryption
- **SSH server:** This establishes secure network connections, undergoes mutual authentication, and initiates encrypted login sessions or file transfers

---

- [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

---

- **Merge commits.** All commits from the feature branch are added to the base branch in a merge commit using the -- no–ff option.
- **Squash and merge commits.** Multiple commits of a pull request are squashed, or combined into a single commit, using the fast-forward option. It is recommended that when merging two branches, pull requests are squashed and merged to prevent the likelihood of conflicts due to redundancy.
- **Merge message for a squash merge.** GitHub generates a default commit message, which you can edit. This message may include the pull request title, pull request description, or information about the commits.
- **Rebase and merge commits.** All commits from the topic branch are added onto the base branch individually without a merge commit.
- **Indirect merges.** GitHub can merge a pull request automatically if the head branch is directly or indirectly merged into the base branch externally.

---

- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

---

- [Google Style Guide](https://github.com/google/styleguide)
- [Reviewing proposed changes in pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request)

---

### Command-line with HTTPS

Install the Git CLI according to your operating system.  
When you push to a GitHub repository over HTTPS, or clone a private repository, Git will prompt you for your GitHub username and password.

If you don’t want to enter your username and password every time,  
you can store them in a file called .netrc in your home directory, like this:

```
machine GitHub.com
    login my-username
    password my-password


machine api.GitHub.com
    login my-username
    password my-password
```

---

### GitHub Project Management Tools

- [A Quick Guide to Using GitHub For Project Management](https://www.jobsity.com/blog/a-quick-guide-to-using-github-for-project-management)
- [GitHub for project management](https://openscapes.github.io/series/core-lessons/github/github-issues.html)
- [Using GitHub as your Project Management Tool | Learn with Dr. G](https://www.youtube.com/watch?v=qgQAFP6oSKw)
- [GitHub Issues: Project Planning for Developers](https://github.com/features/issues)

#### Additional Tools

- [Open source DIY ethics](https://www.arp242.net/diy.html)
- [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
- [Setting guidelines for repository contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [What is CI/CD? Continuous integration and continuous delivery explained](https://www.infoworld.com/article/2269266/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html)
- [CI/CD: What It Is and What You Need to Know](https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/)
- [Travis CI Tutorial](https://docs.travis-ci.com/user/tutorials/tutorials-overview/)
- [Travis CI Build Stages](https://docs.travis-ci.com/user/build-stages/)
