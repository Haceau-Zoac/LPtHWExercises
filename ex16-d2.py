from sys import argv

script, filename = argv

file = open(filename)

print(f'File {filename}:')
print(file.read())

file.close()
