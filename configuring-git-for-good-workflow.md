# Configuring Git for a good workflow

## Git branch autocompletion

## Rich commit messages: Setting the default commit message editor

Often we make commits this way: `git commit -m "here is my commit message"`. But sometimes we want rich, multi-line commit messages, and, later, for things like git rebase we will want to be able to write & read commit messages in our editor, and make rich, multi-line messages.

If you have not, let's configure git globally (for all repos on your computer) to use VS Code as its default editor for commit messages. First though, let's see what your current default editor for commit messages is. Run:

```bash
git config --global core.editor
```

It will probably say `code --wait` (VS Code), `nano`, or `vim`. Note its current setting so you can change it back if desired.

Now run:

```bash
git config --global core.editor "code" --wait
```

**IMPORTANT: If you don't include the `--wait` it will not work!**

Let's confirm this works with a simple commit:

```bash
touch foo.txt
git add foo.txt
git commit
```

This should open up a VS Code window. Write your commit message in it - put in it: 

```txt
Testing git config

Testing the git global config
```

Save and close the file. Run `git status`, you should see something like:

```bash
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)
```

Run `git log`, you should see your commit message:

```bash
commit f016ff965a7360756dcc0ed32d8d4add59927e74 (HEAD -> main)
Author: Adam Cahan <adam.cahan@gmail.com>
Date:   Tue Dec 19 18:55:13 2023 -0600

    Testing git config
    
    Testing the git global config
```

If you want to change your git default global editor back, feel free.

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

## Aliasing common git commands
