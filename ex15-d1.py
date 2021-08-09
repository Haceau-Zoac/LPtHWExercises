# 从 sys 模块导入 argv
from sys import argv

# 读取从控制台输入的参数，分别保存进 script 和 filename 变量中
script, filename = argv

# 打开用户输入的文件，并将文件流保存进 txt
txt = open(filename)

# 打印文件
print(f"Here's your file {filename}:")
# 让 txt 读取文件，并打印出来
print(txt.read())

# 让用户再次输入文件名
print("Type the filename again:")
# 将文件名保存进 file_again 变量中
file_again = input("> ")

# 打开用户再次输入的文件，并将文件流保存进 txt_again
txt_again = open(file_again)

# 让 txt_again 读取文件，并打印出来
print(txt_again.read())