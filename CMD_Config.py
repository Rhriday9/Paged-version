import subprocess
import datetime

def run_command_with_logging(command, test_case_id, name):
    # Capture the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Execute the command and capture the output
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
   
    # Combine output and error messages
    output = stdout.decode() + stderr.decode()

    # Add metadata and format the log entry
    log_entry = f"""
Timestamp: {timestamp}
Test Case ID: {test_case_id}
Name: {name}
Command: {command}
Output:
{output}
"""
    print(log_entry)
    # Store the log entry in a centralized location (e.g., log file)
    with open('command_logs.txt', 'a') as log_file:
        log_file.write(log_entry)
        print('done')
# Example usage
command_to_run = "echo 'Hello, World!'"
print("hello world")
run_command_with_logging(command_to_run, test_case_id="TC123", name="Hello World Test")