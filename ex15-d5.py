print("Type the filename:")
file = input("> ")

txt = open(file)

print(f"Here's your file {file}:")
print(txt.read())