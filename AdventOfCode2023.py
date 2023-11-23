contents = []

with open("myfile.txt", "r") as f:
  for line in f:
    contents.append(line.strip())
    
print(contents)

