import subprocess

repo_path = r"C:\Users\subha\OneDrive\Desktop\Programming\Python"

subprocess.run([
    "C:\\Program Files\\Git\\git-bash.exe",
    "-c", f"""
        cd '{repo_path}' &&
        output=$(git status --porcelain) &&
        
        if [ -z \"$output\" ]; then
            echo 'No changes detected.';
        else
            git status &&
            
            read -p 'Do you want to add all changes? (y/n): ' add_choice &&
            if [ \"$add_choice\" = \"y\" ]; then
                git add . &&
                echo 'Changes added to staging.';
            else
                echo 'Skipping add.';
            fi &&

            read -p 'Do you want to commit? (y/n): ' commit_choice &&
            if [ \"$commit_choice\" = \"y\" ]; then
                read -p 'Enter commit message: ' commit_msg &&
                git commit -m \"$commit_msg\" &&
                echo 'Changes committed.';
            else
                echo 'Skipping commit.';
            fi &&

            read -p 'Do you want to push? (y/n): ' push_choice &&
            if [ \"$push_choice\" = \"y\" ]; then
                git push &&
                echo 'Changes pushed to remote repository.';
            else
                echo 'Skipping push.';
            fi;
        fi &&
        
        exec bash
    """
])