import os

all_dir = os.listdir("C:\\Users\\HP\\PycharmProjects\\Py3xLearning\\ex02_july\\ex_05072024")
print(all_dir)


#Environment Variables

os.environ['My_Var'] = 'Shubham'
print(os.getenv("My_Var"))
