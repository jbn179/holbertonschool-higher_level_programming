#!/usr/bin/python3
"""Script to automate git add, commit and push with flexible file selection"""

import subprocess

def git_operations():
    """Handle git add, commit and push"""
    try:
        # Demander le nom du fichier
        filename = input("Nom du fichier à ajouter (ou '.' pour tout ajouter) : ")
        
        # git add
        subprocess.run(["git", "add", filename], check=True)
        if filename == '.':
            print("Git add de tous les fichiers effectué")
        else:
            print(f"Git add de {filename} effectué")
        
        # Demander le message de commit
        commit_message = input("Message de commit : ")
        
        # git commit -m
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Git commit effectué")
        
        # git push
        subprocess.run(["git", "push"], check=True)
        print("Git push effectué")
        
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors des opérations git : {e}")

if __name__ == "__main__":
    git_operations()
    