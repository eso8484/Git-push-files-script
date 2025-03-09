#!/bin/bash

# Prompt user for commit message
echo -n "Enter commit message: "
read commit_message

# Add all changes
git add .
echo "✔️  Staged all changes"

# Commit changes with the provided message
git commit -m "$commit_message"
echo "✔️  Committed changes: $commit_message"

# Push to the current branch
git push
echo "✔️  Successfully pushed changes."

