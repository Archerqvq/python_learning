# Open the file in read mode
file = open("demofile.txt", "r")  # Replace "file.txt" with the path to your .txt file

# Read the entire contents of the file
contents = file.read()
print(contents)

# Alternatively, you can read the file line by line
# using the readlines() method
lines = file.readlines()
for line in lines:
    print(line)

# Remember to close the file after reading
file.close()
