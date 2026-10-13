
import subprocess

def test():
    assert "2024 is a Leap Year" in subprocess.check_output(
        ["python", "leafyear.py", "2024"], text=True
    )
    assert "1900 is not a Leap Year" in subprocess.check_output(
        ["python", "leafyear.py", "1900"], text=True
    )
    print("All tests passed!")

test()
