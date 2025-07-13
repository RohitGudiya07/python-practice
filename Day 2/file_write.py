# Write to a file and read it back
with open("sample.txt", "w") as f:
    f.write("This is a test file.")

with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)
