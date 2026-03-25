# Git

1. Check the git version

```bash
git --version
```

2. Configure Git

- Configure username

```bash
git config --global user.name ["username"]
git config user.name
```

- Configure email

```bash
git config --global user.email ["email"]
git config user.email
```

3. Initialize a Repository

```bash
git init
```

4. Legends

- U : Untracked
- A : Added
- M : Modified

## Git Three Stage Architecture

1. Check the status of the Repo

```bash
git status
```

2. Add modified files to the Staging Area

```bash
# Add all files
git add .

# Add a specific file
git add [destination_path]
```

3. Create a commit

```bash
git commit -m "[commit_message]"
```

4. Show commit history

```bash
git log
```

```bash
git log --oneline
```

## Reverting vs Resetting

1. Reverting commits

- Creating a new commit that undo the changes from the previous commit

```bash
git revert --no-edit [problematic-commit-hash]
```

2. Resetting commits

- Delete the last commit but it will put all the changes in the working area.
- You have a choice if you want to modify the code or delete the code entirely.

```bash
git reset [second-to-the-last-commit-hash / HEAD~1]
```

## Branching

1. View all the available branches

```bash
git branch
```

2. Create a branch

```bash
git branch [name-of-the-branch]
```

3. Switch to a different branch

```bash
git switch [name-of-the-branch]
```

## Merging

1. Merging branches

```bash
git merge [name-of-the-branch]
```

2. Deleting branches

- Note: You should not be in the branch that you want delete

```bash
git branch -d [name-of-the-branch]
```
