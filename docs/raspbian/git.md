# Git

![github logo](./pics/github.png)

## Git Cheat Sheet

|Command | Definition                  |
|-----   |-----------------------------|
|Init    | Start a repository `git init`|
|Clone   | Create a copy of a repository `git clone git://somewhere.com/something.git [new_name]`|
|Remote  | Display remote repository `git remote -v`|
|Push    | Share changes to an upstream remote (origin) for a branch `git push [origin] [master]`|
|Commit  | One step add/push upstream `git commit -m 'this is my latest update'`|
|Add     | Add files to the repository `git add *.c`. Add is also used to stage files for commit|
|Fetch   | Pull all changes from a remote repository that have been pushed since you cloned it. Note this doesn't merge any of the changes. `git fetch [origin]`|
|Pull    | Will automatically `fetch` and merge changes from upstream into current branch `git pull`|
|Tag     | Create an annotated tag `git tag -a v1.4 -m 'my Version 1.4'`, note for the push command you may have to do: `git push origin v1.4` or `git push origin --tags` to get tags push on upstream server.|
|Status  | Reports the status of untracked changes in your working repository `git status`|
|Diff    | Display changes between working directory and repository `git diff`|
|Rm      | Remove files from repository `git rm file.c`|
|Mv      | Move files `git mv from_file to_file`|
|Log     | View the commit log |

## Git Setup

Let's start off with making git look nice:

    git config color.ui true
    
Since we will work remotely, we need to tell git who we are. Git stores that info in `~/.gitconfig`:

    git config --global user.name "walchko"
    git config --global user.email kevin.walchko@outlook.com

## Working with Git

First clone a repository, make sure you use the `ssh` address and not the default https one:

    git clone git@github.com:walchko/soccer2.git

**Note:** The https one has `https` in the address: `https://github.com/walchko/soccer2.git`

if you accidentally clone the `https` one, you can switch to `ssh` by:

    git remote set-url origin git@github.com:walchko/soccer2.git

Now create ssh keys following the [github directions](https://help.github.com/articles/generating-ssh-keys)

basically:

1. create a key: ssh-keygen -t rsa -C "pi@bender.local"

		pi@bender ~ $ eval "$(ssh-agent -s)"
		Agent pid 12480
		pi@bender ~ $ ssh-add ~/.ssh/id_rsa
		Identity added: /home/pi/.ssh/id_rsa (/home/pi/.ssh/id_rsa)

2. Go to github and add a new ssh key under your profile. Copy/paste in the key (use `more ~/.ssh/id_rsa.pub`) making sure not to add or remove white space.

3. Then try to ssh in:

		pi@bender ~ $ ssh -T git@github.com
		The authenticity of host 'github.com (192.30.252.128)' can't be established.
		RSA key fingerprint is 16:47:ac:a4:76:28:2d:34:63:1b:56:4d:74:7f:76:48.
		Are you sure you want to continue connecting (yes/no)? yes
		Warning: Permanently added 'github.com,192.30.252.128' (RSA) to the list of known hosts.
		Hi walchko! You've successfully authenticated, but GitHub does not provide shell access.

**Success** ... enjoy!

## Git Workflow

Read [this](http://rogerdudler.github.io/git-guide/) awesome guide

1. Make sure your current copy is up to date

        git pull

2. Create a new branch to hold your new feature

        git checkout -b my-cool-new-thing

3. Edit code
4. Mark files for change

        git add *
    
5. Commit files (locally) to HEAD

		git commit -m "what did you do?"
		pi@bender ~/soccer2/IMU $ git push origin master
		Counting objects: 12, done.
		Compressing objects: 100% (8/8), done.
		Writing objects: 100% (8/8), 736 bytes, done.
		Total 8 (delta 6), reused 0 (delta 0)
		To git@github.com:walchko/soccer2.git
		   8162ade..cd9a476  master -> master

6. Push changes upstream, back to the repository so everyone can use them

		git push origin master
    or
		git push origin <branch>
    
To undo what you have committed already and basically create an anti-patch for each commit:

    git revert 0766c053 25eee4ca a867b4af






