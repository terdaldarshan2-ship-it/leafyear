import subprocess
import sys

year = sys.argv[1]

result = subprocess.check_output(
    [sys.executable, "leafyear.py", year], text=True
)

print(result)
print("Test completed!")
