# Welcome to the Intro Class
Please read the following instruction and set up your local environment (Git + python) before Homework 1.

## Recommended workflow:
As we've seen some conflicts with upstream and local changes, let's try to follow the following workflow if possible to make the repo cleaner.

1. After forking the repo, **DON'T** make changes in any existing branches.
2. Make a new branch if you want to make any modification. In this way, your local changes only exist in this new branch.
3. Whenever the upstream repo is updated, you can `fetch` upstream and merge changes into your local branches.
4. Then you can `merge` changes into the new branch with your work, or `rebase` your new branch on updated branch (now synced with upstream).
5. You will push all your changes to the new branch you created, not existing branches in the synced fork. This way, then branches in your fork only have changes from upstream so no conflict will occur.

## Setting up your forked repo:

1. In terminal/command line, navigate to the folder you want to put this repo.

2. **[Only required for first-time setup]**: Fork the [class repo](https://github.com/DS-XL/ds-intro-class-2022) to your GitHub account. Your repo should look something like  
	`https://github.com/YOUR_USERNAME/ds-intro-class-2022`

3. **[Only required for first-time setup]**: Clone the **forked repo** to your local directory and enter your local repo directory
 
	```
	cd [YOUR DESTINATION DIRECTORY] # navigate to destination on local laptop
	
	git clone https://github.com/YOUR_USERNAME/ds-intro-class-2022
	
	cd ds-intro-class-2022
	```

4. **[Only required for first-time setup]**: [Configure remote for the fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork) following the instructions
	- Check you remote of your fork: `git remote -v`
	- Specify the class remote(`https://github.com/DS-XL/ds-intro-class-2022`) as upstream repo that will be synced wih your fork. 
	  `git remote add upstream https://github.com/DS-XL/ds-intro-class-2022.git`
	- Verify the new upstream repository you've specified for your fork by running `git remote -v` again. You should now see at least 4 of them including `upstream` pull and fetch, and `origin` pull and fetch.
	
5. **[Do this whenever you'd like to add upstream changes to your forked repo]**. [Sync a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) to get the latest updates from class repo.
	
	- Fetch the branches and their respective commits from the upstream repo by running `git fetch upstream`
	- If you'd like to update your forked remote with upstream changes, you can merge in and push the upstream changes to your branch in the forked remote.
	
		```
		# assuming your local has an older version of [branch_name] branch
		git checkout [branch_name]
		git merge upstream/[branch_name] [branch_name]
		git push origin [branch_name]
		```

	- If you have modified files in your local branch `[branch_name]` you might [have a conflict that prevents you from merging](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts). There are a few ways to resolve the conflict:
		- [Resolve through command line](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line): After resolving the conflict, stage and commit your changes. Now you can merge or push changes to `origin`
		- Instead of using `git merge`, use `git rebase`. `rebase` is like changing the "reference point" of you commit. Instead of using `origin/[branch_name]` as base for change, now you can ask Git to use the new `upstream/[branch_name]` so changes on both sides are included. If you want to use this, instead of the code block above, use the following:

			```
			# assuming your local has an older version of [branch_name] branch
			git checkout [branch_name]
			git rebase upstream/[branch_name]
			git push origin [branch_name]
			```
		- Create a *new branch* altogether with your local changes and the upstream. It could look something like this but it could be up to you to decide.

			```
			# create a new branch based on upstream
			git branch [new_branch_name] upstream/[branch_name]
			git checkout [new_branch_name]
			
			# merge local branch in
			git merge [branch_name]
			git push origin [branch_name]       # this will apprea as a new branch
			```
			
6. Now you have successfully synced your local and your forked repo with upstream.	
7. You can now work on your local repo, remember to track and commit your changes like below.

	```
	git status
	git add [files to add]
	git commit -m "[message goes here]"
	git push origin [branch_name]
	```
*Note*:  you are **ALWAYS** pushing to remote, make sure you are pushing to **your forked repo** as you don't have access to the class repo (this should be your `upstream` instead). Run `git remote -v` to check your remote settings and add/remove/modify as need.

	
	
## Instructions for Homework 1 Submission:
1. Create a new local branch named `homework01`. You will be working on your homework on this branch.
2. Create a new jyputer notebook for `Exercise 3` and `Exercise 4`. Copy/Paste the problems is optional, but at least number your answers so we know which problem it is.
3. Push your commits on the new branch `homework01` to your remote forked repo (you've learned this in above).
4. Pull request your answers to `homework01` branch in you own forked repo following [Creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
5. Pull request your answers to `master` branch in my class repo (upstream) following [Creating a pull request from a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork). 
	
*Hint: you can try creating a branch from a specific branch by `git checkout -b [new branch name] [old branch name]`*