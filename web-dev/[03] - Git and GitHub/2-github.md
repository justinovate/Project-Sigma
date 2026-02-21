# GitHub

## Create a Remote Repository

1. Visit GitHub and Login.
2. Click the `New Button` on the top left.
3. **Create a repository** page.
   - Repository name: [cohort-batch-number]
   - Status: Public or Private
     - Choose `Public`.
   - Make sure that `Add a README file` checkbox is NOT ticked.
   - Click the `Create Repository` button.
     - You will be redirected to `Quick Setup` page.
4. **Quick setup** page.
   1. Make sure that you are using `HTTPS` and NOT `SSH`.
      - Both are **Network Protocol**:
        - Hypertext Transfer Protocol Secure (HTTPS).
        - Secure Socket Shell (SSH)
   2. Create a connection between `Local` and `Remote` repository.
      1. Create a new repository on the command line.
      2. Push an existing repository from the command line. (SELECT THIS!)

## Steps:

1. Create a connection between local and remote repository.

```bash
git remote add origin [repository-url]
```

2. Rename the master branch to main

```bash
git branch -M main
```

3. Push commits to the remote repository for the first time
   - **-u flag:** Initial Push

```bash
git push -u origin main
```

4. Next commits pushed to the remote repository

```bash
git push
```
