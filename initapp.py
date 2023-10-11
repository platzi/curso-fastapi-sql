import subprocess
from typing import List, Tuple, Union

def execute_command(command: str) -> Tuple[bool, Union[str, str]]:
    try:
        # Execute the command and capture standard output and errors
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # Check if there were errors during execution
        if process.returncode == 0:
            # Success: the command ran without errors
            return True, stdout
        else:
            # Error: the command returned a non-zero exit code
            return False, stderr
    except Exception as e:
        # Error during command execution
        return False, str(e)

def execute_commands(commands: List[str]) -> List[Tuple[bool, Union[str, str]]]:
    results = []
    for i, command in enumerate(commands, start=1):
        success, result = execute_command(command)
        results.append((success, result))
        status = 'executed successfully' if success else 'error during command execution'
        print(f"Command '{command}': {status}")
        print(result)

    return results

# Example of usage
commands = [
            "ls -la",
            "echo 'Hello, World!'",
            "date",
            "git add ."
            ]
results = execute_commands(commands)
