# Git Push Automation Script

## Description
This script automates the process of adding, committing, and pushing changes to a Git repository with a custom commit message.

## Installation
1. Save the script as `git_push.sh`.
2. Move it to a directory in your system's `PATH` and rename it for easy access:
   ```bash
   sudo mv git_push.sh /usr/local/bin/gp
   ```
3. Make the script executable:
   ```bash
   sudo chmod +x /usr/local/bin/gp
   ```

## Usage
1. Navigate to any Git repository.
2. Run the script by typing:
   ```bash
   gp
   ```
3. Enter your commit message when prompted.
4. The script will:
   - Stage all changes (`git add .`)
   - Commit the changes with your message (`git commit -m "your message"`)
   - Push the changes to the remote repository (`git push`)

## Example
```bash
$ gp
Enter commit message: Updated README with new instructions
✔️  Staged all changes
✔️  Committed changes: Updated README with new instructions
✔️  Successfully pushed changes.
```

## Notes
- Ensure you are inside a valid Git repository before running the script.
- You must have the necessary permissions to push changes to the remote repository.
- If using SSH authentication, make sure your SSH key is set up for Git.

## License
This script is free to use and modify.

## **🌐 Connect With Me**

[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/oche_21)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/eso8484)
[![Direct Contact](https://img.shields.io/badge/Direct_Contact-%23009688.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/eso8484)
