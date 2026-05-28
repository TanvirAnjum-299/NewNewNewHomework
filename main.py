# Read mode
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Write mode
with open("data.txt", "w") as f:
    f.write("Hello, Ayub!\n")

# Append mode
with open("data.txt", "a") as f:
    f.write("Adding more lines...\n")

# Read + Write mode
with open("data.txt", "r+") as f:
    old = f.read()
    f.write("\nNew content after reading.")
