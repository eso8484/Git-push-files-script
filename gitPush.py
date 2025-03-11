#!/usr/bin/env python3

import sys
import os

def git_push_files(commit_messages):
    print("Adding all files")
    os.system("git add .")

    print("Committing changes")
    os.system(f'git commit -m "{commit_messages}"')

    print("Pushing files to remote server")
    os.system("git push")

    print("All changes pushed to remote server successfully")

def main():
    if len(sys.argv) > 1:
        commit_m = " ".join(sys.argv[1:])  # Fixed extra space issue
    else:
        commit_m = input("Enter commit message: ")
    
    git_push_files(commit_m)

if __name__ == "__main__":
    main()

