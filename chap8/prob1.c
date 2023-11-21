text_file = open("read_it.txt", "r")

print("Opening and closing the file.\n")
print("Reading character from the file.")
print(text_file.read(1))
print(text_file.read(5))

print("\nReading the entire file at once.")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)

print("\nReading characters from a line.")
text_file = open("read_it.txt","r")
print(text_file.readline(1))
print(text_file.readline(5))

print("\nReading one line at a time.")
text_file = open("read_it.txt","r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
print()

print("\nReading the entiro file into a list.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)

print(len(lines))
for i in lines:
    print(i)
print()

print("\nLooping through the file, line by line.")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
    print()

text_file.close()



