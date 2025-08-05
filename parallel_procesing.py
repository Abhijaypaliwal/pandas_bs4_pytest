
import subprocess
import concurrent.futures

def run_command(cmd):
    result = subprocess.run(cmd, capture_output = True, text = True, shell = True)
    return result.stdout

commands = [
    "echo Command1",
    "echo Command2",
    "echo Command3",
    "ping -n 3 google.com",
    "ls"
]
with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
    results = list(executor.map(run_command, commands))

for output in results:
    print(output)
    print("-" * 40)