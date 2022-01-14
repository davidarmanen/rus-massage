import os

arr = os.listdir("C:/fb")
for i in arr:
    with open(f"C:/fb/{i}", "r") as f:
        text = f.read()
    with open("fb.txt", "a") as f:
        f.write(text)
