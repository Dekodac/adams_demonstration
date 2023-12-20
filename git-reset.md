The commands we'll examine are:
- `git restore`
- `git reset`
- `git log`
- `git diff`

The concepts we'll look at are:

- `HEAD`
- Commit hashes & Refs
- "The Three Trees"
- Force-pushing

The scenario's we'll see how to handle:

1. "I staged (added) code I don't want to commit, but I didn't commit it yet." --> `git restore --staged`
We will focus on `git restore --staged`, `git reset --soft`, and with caution, force-pushing, and, `git reset --hard`.
We'll see how to use `git restore --staged` safely in this scenario.
### Use `git restore --staged` to un-stage changes
We will **not** do `git restore --staged .`, as, the "." pattern will un-stage *all* files and if we make a mistake and use `reset --hard` instead of `restore --staged` we'll lose all our work!
Run this command: `git restore --staged .venv`. We have just told git to un-stage the `.venv` directory, and only the `.venv` directory. Even if we screw up the reset command, being more specific limits the risk. Let's run `git status` and see how we did.
What is the `~1` part? The tilde (`~`) and the number indicate **how many commits back** this command should be run.
Let's use the `git diff` command, which *compares* commits, to examine this. Git diff lets us compare **between commits**, and between our "Staged Area" or Index code and commits. Run:

```
cd ../backend
echo "print('hello') > foo.py
git diff HEAD
```

We just created a file `foo.py`, but it's not staged yet. Diffing against HEAD (most recent commit shows nothing). Run:

```bash
git add foo.py
git diff HEAD
```

You should see:

```
diff --git a/backend/foo.py b/backend/foo.py
new file mode 100644
index 0000000..ed0f110
--- /dev/null
+++ b/backend/foo.py
@@ -0,0 +1 @@
+print('hello')
```

Our Index (staged/added code), has a *difference* relative to our most recent commit, now that we've added `foo.py`.

Run `git diff HEAD~1`, and then `git diff HEAD~2`. You should see a bunch of code printed out. This is the *difference* between our index/current head and the previous commit, or the difference from 2 commits back, and so on.

Use the git graph VS Code plugin to help visualize our branch history:

![initial-setup-branch](./page-resources/git-graph-initial-setup-2-commits.png)

Go ahead and `rm foo.py` and run `git diff HEAD~1` and `git diff HEAD~2` again - we are comparing our `HEAD` commit against other previous commits on the branch!

#### Running git reset --soft

Now that we understand our command, let's use it! But first, a backup branch in case we error:

```bash
git status
git checkout -b wip-initial-setup-backup
git checkout -
```

`git checkout -` is a useful command that switches us back to the last branch we used. We now have a backup branch, in case our reset command goes wrong. Run:

```bash
git reset --soft HEAD
git status
```

You should see:

```bash
On branch initial-setup
Your branch is up to date with 'origin/initial-setup'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .env
        modified:   app.py
        modified:   requirements.txt
```

In git graph you should see:
![initial-setup-reset-soft](./page-resources/initial-setup-reset-soft.png)
We have:
- Un-commited our last commit on our branch without losing code. We can now modify it.
- We still have that commit on a backup branch, in case something goes wrong.
Run:
```bash
git restore --staged .env
git status
git commit -m 'Add dotenv to flask'
git status
git push
```
And now we have removed the `.env` file from our last commit! And done so safely.
## Scenario 3: I committed code I don't want **and** pushed it **Caution!!!**

This scenario requires extra caution and we will see how to safely handle it using `git reset --soft` and a force push.
### Concepts

- The "Three Trees": Working Directory, Staging Directory / Index, HEAD

- Working Directory

- The Index or "Staging Area"

- What is a commit? What is a commit hash?

- What is HEAD?

1. Does `git restore --staged` ever delete code entirely from our repo? Does it remove code from the "Working Directory"?
[Git restore](https://stackoverflow.com/questions/58003030/what-is-the-git-restore-command-and-what-is-the-difference-between-git-restor)
