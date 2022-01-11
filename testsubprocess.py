import subprocess

if __name__ == "__main__":
    subprocess.run(["ls", "-l"])
    for i in [2,5,6,8]:
        subprocess.run(["python", "python_scrip_101.py", "9", "--x", f"{i}", "--yval", "2"])