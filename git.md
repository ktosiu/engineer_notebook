# Git Cheat Sheet

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

