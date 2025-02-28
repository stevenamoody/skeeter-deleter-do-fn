import subprocess

def run_skeeter_deleter():
    try:
        # Call the skeeter-deleter CLI utility with the specified arguments
        result = subprocess.run(['skeeter-deleter', '-s', '2', '-y'], check=True, text=True, capture_output=True)
        
        # Print the output of the command
        print("Output:", result.stdout)
        
        # Print any errors (if they occur)
        if result.stderr:
            print("Errors:", result.stderr)
    
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the execution of the command
        print(f"An error occurred: {e}")
        print("Command output:", e.output)
        print("Command stderr:", e.stderr)

if __name__ == "__main__":
    run_skeeter_deleter()
