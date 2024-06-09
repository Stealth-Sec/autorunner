#Runner
print("Test 1 Sucessfull")
import time
time.sleep(10)
print("Test 2 Sucessfull")
import subprocess
subprocess.run(["pip", "install", "selenium"])
if subprocess.returncode == 0:
    print("Test 3 Sucessfull")
else:
    print(f"Failed to install Selenium using pip. Return code: {subprocess.returncode}")
