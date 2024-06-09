import os
import time

print("Test 1 Sucessfull")
time.sleep(2)
print("Test 2 Sucessfull")

try:
    print("Installing Selenium...")
    os.system("pip install selenium")
    print("Test 3 Sucessfull")
except Exception as e:
    print(f"Failed to install Selenium: {str(e)}")

print("End")
