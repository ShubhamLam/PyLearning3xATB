#Walk me into Directory
import os

for root, dir, files in os.walk("C:\\Users\\HP\\PycharmProjects\\Py3xLearning\\ex02_july\\ex_05072024"):
    print(f"Current Dir{root}")
    print(f"Sub Current Dir{dir}")
    print(len(files))
