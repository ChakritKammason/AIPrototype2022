import subprocess

if __name__ == "__main__":
    #subprocess.run(["ls", "-l"])
    #for i in [2,5,6,8]:
    #    subprocess.run(["python", "python_scrip_101.py", "9", "--x", f"{i}", "--yval", "2"])


    ##use ouput of subprocess
    #pro = subprocess.Popen(["ls", "-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out, err = pro.communicate()
    #print(out)

    #HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูณ
    for i in [2,5,6,8,]:
        process = subprocess.Popen(["python", "python_scrip_101.py", "9", "--x", f"{i}", "--yval", "2"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        print(str(out))

