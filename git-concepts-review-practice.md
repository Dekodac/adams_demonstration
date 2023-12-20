# Git Concepts: Review & Practice

## Prequesites

- Install the [git graph VS Code Extension](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- This is not an "Intro to git" - you should have some basic experience, and we will dive a bit deeper.

## Goals

You will learn a number of git techniques which will improve your coding productivity and workflow. Our focus will be more on working on your "own" branch, and we will get into collaborative work, branching strategies, and some basic merge conflict strategies later.

These conceptual fundamentals & techniques will be useful when using git collaboratively on a team as well as when working by yourself.

## Preview: Let's make a "feature branch", push it, PR it, and merge it!

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

## Configuring git for a good workflow

### Git branch autocompletion
### Setting the default commit message editor

If you have not, let's configure git globally (for all repos on your computer) to use VS Code as its default editor for commit messages. Run:

```bash
git config --global core.editor "code"
```

Let's confirm this works with a simple commit:

```bash
touch foo.txt
git add foo.txt
git commit
```

This should open up a VS Code window. Write your commit message in it - put in it: 

```
Testing git config

Testing the git global config
``` 

Save and close the file. Run:

```bash
git status
git log
```


Note that there is a `.gitconfig` directory in my OS user's *home directory*, in the above example `/Users/adamcee/.gitconfig`.

There are a number of global configuration settings we can make for git. We will not cover them all here, but, let's see *where our global git config files live*, and, see some of what's in them. Run:

```bash
git config --list --show-origin
```

What you see will be different - it will depend on your OS username and other details, some of it will look like this:

```bash
file:/Library/Developer/CommandLineTools/usr/share/git-core/gitconfig   credential.helper=osxkeychain
file:/Library/Developer/CommandLineTools/usr/share/git-core/gitconfig   init.defaultbranch=main
file:/Users/adamcee/.gitconfig  user.email=adam.cahan@gmail.com
file:/Users/adamcee/.gitconfig  user.name=Adam Cahan
file:/Users/adamcee/.gitconfig  init.defaultbranch=main
file:/Users/adamcee/.gitconfig  core.editor=code
file:.git/config        core.repositoryformatversion=0
```



### Aliasing common git commands

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

### Git reset - deleting unstaged code. *Caution!!!*

### Git reset hard - overwring my local branch with remote branch. *Caution!!!*

### Advanced technique: `git rebase -i` and force-push *Caution!!!*

## "Time travel" - checking out a previous commit, changing stuff
### Make a backup branch
### `git checkout <COMMIT_HASH>`
### `git checkout HEAD~1`
### Making a new branch with changes
### "Going back" - getting back to HEAD

## Techniques for working with branches / existing commits

### Use git cherrypick to copy a commit from one branch to another
