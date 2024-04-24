# What is Git?
Git is, in short, a version control software. Read [a short intro to Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) to understand how it does version control.

*Additional reading*: Atlassian's [What is version control](https://www.atlassian.com/git/tutorials/what-is-version-control)

# Why is version control useful?
* **Backup your work** 
* **Collaborate with others** 

# Installing Git
Check out [this page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for instructions on how to install Git on your laptop. 

For MacOS, you might already have Git, you can check by running `git --version` in your command line and see. For Windows, it's likely you'll need to install Git for Windows per web page above. For a bit more detail, you can refer to [this second page](https://www.atlassian.com/git/tutorials/install-git#windows) with step-by-step instructios.

Make sure you have the command line tool (terminal) but not the GitHub GUI desktop version. After installation, make sure your `git` is working by running `git --version` in your terminal.


# GitHub 
[GitHub](https://github.com/) is a place to host Git repositories:

> GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

If you do not have a GitHub account yet, please go ahead and create one. Follow the instructions in account set up to configure your local Git. If you need help, [this page with instructions to set up and authenticate](https://help.github.com/en/github/getting-started-with-github/set-up-git) might be a good source to check how to configure user name and account in Git. Generally you can choose to [use HTTPS with password caching](https://help.github.com/en/github/using-git/caching-your-github-password-in-git) or [generat and add SSH key](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to ssh-agent.

If you're interested, spend 10 min to read and follow [this `Hello-Would` tutorial](https://guides.github.com/activities/hello-world/) to get some initial ideas for version control, repos, and how to use GitHub. 

# Git basics
## First things first
### Git configuration
The first thing you should if probably set up your user name and email address. This is important because every Git commit uses this information:

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
As you probably see here, the `--global` option here will allow Git always use that information for anything you do on that system. If you want to override this with a different name or email address for specific projects, you can run the command without the `--global` option when you’re in that project.

You can use `git config --list` to check current configuration of your Git.

### Get an existing repo
Creating a local copy of a Git repo. Nagivate to the directory where you want to store the repo (`cd <your/path/to/local/directory>`), then 

`git clone <repo url goes here>`
### Create a new repo
You can also create a new repo from sratch. In the directory you hope to create a repo for, do the following to initiate a new repo

`git init <project name goes here>`

## Using Git
![Git Flow](https://git-scm.com/book/en/v2/images/areas.png)

The Git **directory** is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you `clone` a repository from another computer.

The basic Git workflow goes something like this:

* You modify files in your working directory (sometime we refer to this as **local**).

* You selectively stage just those changes you want to be part of your next `commit`, which adds only those changes to the staging area.

* You do a `commit`, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

If a particular version of a file is in the Git directory, it’s considered *committed*. If it has been modified and was added to the staging area, it is *staged*. And if it was changed since it was checked out but has not been staged, it is *modified*. In the next section, you’ll learn more about these states and how you can either take advantage of them or skip the staged part entirely.

## Making and recording changes to the files
Once a repo is created for your working directory, each file in your working directory will be in one of the following statuses:  untracked, unmodified, modified, or staged. Tracked files are files that Git knows about, while untracked files are not known by the repo before added.

![](https://git-scm.com/book/en/v2/images/lifecycle.png)

You can use `git status` to check the status of the files in working directory any time.

## Understanding `local` and `remote`
You can do the version control 100% on your local repo using Git. You can navigate between `local` and `remote` to keep track of changes as well as collaborate.

![](https://github.com/Tian-Su/intro_to_data_science_2017/blob/master/figures/github_fork_pull_request.png?raw=true)

## When you’re ready to `push` code

### 1. See what’s changed since the last commit
`git status` shows files that have changed or are untracked
`git diff [optional: filename]` shows the changes themselves (e.g. color-coded deletions and additions)

### 2. “Stage” the things you want to include in your commit
This includes both files that have changed and new files you want to add to "staging area".

`git add <file or directory>`

If you want to add everything in the working directory, you can use shortcut `git add .`, there will include everything except for listed in `.gitingore` if you have one.

You can use `git diff --cached` to check what you've staged so far.

### 3. Commit your changes and add a useful message

`git commit -m ‘message goes here’`
The message should be a short summary of what the changes are. If you don't use the `-m` option, Git will launch your text editor for you to enter the message. 

### 4. (optional) Pull from the origin repo

`git pull`

If any other changes were made since you last pulled, this will attempt to merge them with yours. If you don’t do this and you need to, the remote repo will tell you.

### 5. Push to the remote repo
Remote repositories are versions of your project that are hosted on the Internet (e.g. GitHub) or network somewhere. You'll need a remote repo to collaborate with others. 

You can check your remote for a repo by `git remote`. You'll probably see`origin` as it is the default name Git gives to the server you cloned from.

`git push <remote> <branch>`

This command pushes the changes you have commited to the remote. If you have the remote hosted on GitHub, you'll see the changes there now.

## How to undo things
### Unstage a Staged File
`git reset -HEAD <file name>`

### Unmodifying a Modified File (DANGER!)
> It’s important to understand that git checkout -- <file> is a dangerous command. Any local changes you made to that file are gone — Git just replaced that file with the most recently-committed version. Don’t ever use this command unless you absolutely know that you don’t want those unsaved local changes.

You will revet the file to its last commit but will lose all untracked uncommited changed.
`git checkout -- <file name>`

### Revert/Reset a commit
`git revert HEAD`

`git reset HEAD^`
 
 
## Additional useful commands
### `git remote add <shortname> <url>`
Add remote to repo.
### `git log`
See the history of commits present in your copy of the repo.
### `git rm`
Remove a file from the repo. If you'd like to remove a file from Git repo but not your local directory, learn about `git rm --cache`.
### `git mv`
Rename/move a file in the repo
### `git stash`
Save your changes to a “stash”, but don’t commit them. Useful if you might want to come back to things later, but want to wipe your changes clean right now.
### `git branch`
List all the branches for the repo. The current one will have a * next to it.

### `git branch <branch name>`
Create a new branch with <branch name>.

**Note**: this will only create the new branch but will not automatically switch to the new branch. Use `git checkout -b <branch name>` for creating and checking out new branch at the same time.

### `git checkout <revision #, or branch name> <optional filename>`
If you give a revision number, this changes your files to how they were when that commit was the latest. Think of this like a time machine for going to old commits, without changing/losing anything in the present repo.

If you give a branch name, `git checkout` will switch you to the most recent commit in that named branch and make that branch the active one (so new commits will be added to that branch)

**WARNING:** if you specify a file, using `git checkout` without committing your latest changes will wipe them out.

## Advanced: Branching+Merging Basics
Let's walk through [a scenario](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) as example:

> Let’s go through a simple example of branching and merging with a workflow that you might use in the real world. You’ll follow these steps:
> 
* Do some work on a website.
>
* Create a branch for a new user story you’re working on.
>
* Do some work in that branch.
> 
At this stage, you’ll receive a call that another issue is critical and you need a hotfix. You’ll do the following:
> 
* Switch to your production branch.
> 
* Create a branch to add the hotfix.
> 
* After it’s tested, merge the hotfix branch, and push to production.
> 
* Switch back to your original user story and continue working.

![](https://git-scm.com/book/en/v2/images/basic-branching-1.png)
![](https://git-scm.com/book/en/v2/images/basic-branching-3.png)
![](https://git-scm.com/book/en/v2/images/basic-branching-4.png)
![](https://git-scm.com/book/en/v2/images/basic-branching-5.png)
![](https://git-scm.com/book/en/v2/images/basic-branching-6.png)
![](https://git-scm.com/book/en/v2/images/basic-merging-1.png)
![](https://git-scm.com/book/en/v2/images/basic-merging-2.png)

On the branch you'd like to merge into: `git merge <branch to be merged in>`


## Git Cheatsheet
[PDF](https://education.github.com/git-cheat-sheet-education.pdf)

## Interactive tutorial (highly recommend!)
You can learn the basic ideas about version control, commits, branching, merging, pushing, and more at [https://learngitbranching.js.org/?locale=en_US](https://learngitbranching.js.org/?locale=en_US)

Recommend at least finish the first 8 levels in `Main` tab and the first 4 in `Remote` tab.