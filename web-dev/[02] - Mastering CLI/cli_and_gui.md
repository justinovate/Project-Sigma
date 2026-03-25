# GUI and CLI

1. Graphical User Interface (GUI)

- Use graphical components such as Icons, Buttons, Menus to interact with our machine.

2. Command Line Interface (CLI)

- Use text-based commands to interact with our machine.
  - Windows: Default terminal is powershell.
  - Mac: Default terminal is zsh (Z-shell).

## Directory Management and Navigation

1. Create a directory

- Note: If the directory name contains space, encapsulate it using either '' or "".

```bash
mkdir [directory_name]

# Create Multiple Directories
mkdir [directory_name] [directory_name] [directory_name]
```

2. Delete a directory

```bash
rmdir [directory_name]
```

3. Print working directory

```bash
pwd
```

4. List command

```bash
# list all the files and folders inside the current folder.
ls
```

5. Change directory

```bash
cd [directory_name]
```

6. Go back to parent directory

```bash
cd ..
```

## File Operations

1. Create a file

```bash
touch [filename.extension]
```

2. Delete a file

```bash
rm [filename.extension]
```

3. Rename a file

```bash
mv [current_filename.extension] [new_filename.extension]
```

4. Move a file

```bash
mv [filename.extension] [new_directory_path]
```

5. Display the contents of the file

```bash
cat [filename.extension]
```

6. Display the first 10 lines of a file

```bash
head [filename.extension]
```

7. Display the last 10 lines of a file

```bash
tail [filename.extension]
```

8. Display nth number of lines of a file

```bash
[head/tail] -n [number_of_lines] [filename.extension]
```

## Searching

1. Check the files, directories, and subdirectories of the current directory

```bash
find .
```

2. Check the files inside the current directory

```bash
find . -type f
```

3. Check the directories inside the current directory

```bash
find . -type d
```

4. Search for a specific file

```bash
find . -name [filename.extension]
```
