# Step 1: Open file in write mode
f = open("example.txt", "w")

# Step 2: Write data
f.write("This is Part 2 of File Handling.\n")

# Step 3: Append more data
f = open("example.txt", "a")
f.write("Appending new content...\n")

# Step 4: Read the file
f = open("example.txt", "r")
print(f.read())

# Step 5: Check cursor position
print("Cursor at:", f.tell())

# Step 6: Reset cursor to start
f.seek(0)
print("After seek:", f.read())

# Step 7: Close file
f.close()
