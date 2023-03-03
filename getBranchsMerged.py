import subprocess

# Run the git command and capture the output
command = "git branch --merged master"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Decode the output and split it into a list of branches
merged_branches = stdout.decode().split()

# Print the list of branches
print("Merged branches in master:")
for branch in merged_branches:
    print(branch)
