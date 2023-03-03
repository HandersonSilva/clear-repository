import subprocess

# Replace "ls -l" with the command you want to run
command = ""

# Run the command
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the process to finish and get the output
stdout, stderr = process.communicate()

# Print the output
print(stdout.decode())
