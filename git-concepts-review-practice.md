# Notes & Outline: Git Concepts: Review & Practice

## Git Concepts Review

### How does git save / keep track of my code?
#### Unstaged
#### Staged
#### Committed

### What is a commit? What is a commit hash?
### What is `HEAD`?
### What is a branch?

## Techniques: Being a Github power-user

### Looking at different branches
### Looking at a branch's commit history
### Looking at a specific commit
### Sharing a link to a specific LoC (line of code)
### Looking at the whole repo at a specific point in time (a specific commit)
### Global search
### Editing in Github: When to do it, When *NOT* to do it

## Techniques to explore your code with git
### `git log` to look at your branch history
### `git diff` - compare commits
### `git grep` to search your codebase (and ignore your dependencies! :) )

## Techniques while coding & making new commits

### Commit often, push often

### Staging a single file, all files, or some files w/patterns

### Unstaging code safely

### "Backup Branches", "Prototype Branches" and, "Branch early, branch often"

### Use `git checkout -` to hop between branches quickly

### Use git stash to move unstaged changes between branches

### Git reset - deleting unstaged code. -- *Caution!!!*

### Git reset hard - overwring my local branch with remote branch. -- *Caution!!!*

### Advanced technique: `git rebase -i` and force-push -- *Caution!!!*

## "Time travel" - checking out a previous commit, changing stuff
### Make a backup branch
### `git checkout <COMMIT_HASH>`
### `git checkout HEAD~1`
### Making a new branch with changes
### "Going back" - getting back to HEAD

## Techniques for working with branches / existing commits

### Use git cherrypick to copy a commit from one branch to another
