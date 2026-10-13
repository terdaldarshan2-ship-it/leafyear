
import subprocess

def test():
    year = input("Enter a year to test: ")

    out = subprocess.check_output(
        ["python", "leafyear.py", year], text=True
    )

    print(out)
    print("Test completed!")

test()
