import subprocess

# Run the git command and capture the output
command = "git branch --no-merged main"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Decode the output and split it into a list of branches
unmerged_branches = stdout.decode().split()

# Print the list of branches
print("Unmerged branches in master:")
for branch in unmerged_branches:
    print(branch)
