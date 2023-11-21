print("Creating a text file with the write<> method.\n")

print("Reading the newly created file.")
text_file = open("write_it.txt", "w")
text_file.write("line 1\n")
text_file.write("This is line 2\n")
text_file.write("And that would make this the third line.\n")
text_file.close()

text_file = open("write_it.txt","r")
print(text_file.read())

text_file = open("writes_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

print("Creating a text file with the write<> method.\n")
print("Reading the newly created file.")
text_file = open("writes_it.txt", "r")
print(text_file.read())
