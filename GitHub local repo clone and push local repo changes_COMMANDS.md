# On first run, create virtual environment:
conda activate dev

# Navigate into Desktop:
cd Desktop

# Clone virtual GitHub repo to local Desktop:
git clone https://github.com/K-G-Witt/python-challenge.git

# Navigate into newly created local repo:
cd python-challenge

# Create a new subfolder called 'PyBank':
mkdir PyBank

# Create a new subfolder called 'PyPoll':
mkdir PyPoll

# Navigate into subfolder 'PyBank':
cd PyBank

# Create a new .py file called 'main':
touch main.py

# Create a new sub-subfolder called 'Resources':
mkdir Resources

# Navigate into sub-subfolder 'Resources':
cd Resources

# Create a placeholder file in 'Resources':
## Necessary as push command will not allow empty folders to be pushed back to GitHub:
touch placeholder_file1.txt

# Navigate back into sub-folder 'PyBank':
cd ..

# Create a new sub-subfolder called 'Analysis':
mkdir Analysis

# Navigate into sub-subfolder 'Analysis':
cd Analysis

# Create a placeholder file in 'Analysis':
## Necessary as push command will not allow empty folders to be pushed back to GitHub:
touch placeholder_file2.txt

# Navigate back into sub-folder 'PyBank':
cd ..

# Navigate back into folder 'python-challenge':
cd ..

# Navigate into folder 'PyPoll':
cd PyPoll

# Create a new .py file called 'main':
touch main.py

# Create a new sub-subfolder called 'Resources':
mkdir Resources

# Navigate into sub-subfolder 'Resources':
cd Resources

# Create a placeholder file in 'Resources':
## Necessary as push command will not allow empty folders to be pushed back to GitHub:
touch placeholder_file3.txt

# Navigate back into sub-folder 'PyPoll':
cd ..

# Create a new sub-subfolder called 'Analysis':
mkdir Analysis

# Navigate into sub-subfolder 'Analysis':
cd Analysis

# Create a placeholder file in 'Analysis':
## Necessary as push command will not allow empty folders to be pushed back to GitHub:
touch placeholder_file4.txt

# Navigate back into sub-folder 'PyPoll':
cd ..

# Navigate back into folder 'python-challenge':
cd ..

# Commit all these changes:
git add .
git commit -m "PyBank and PyPoll Subfolders Created"

# Push these changes in 'python-challenge' GitHub repo:
git push -u origin main
