print("Iput your string . . .\n")

text_file = open("p3.txt", "w")

while True:
    n = input(">>")
    if(n != "Q"):
        text_file.write(n+"\n")
    else:
        break
text_file.close()
text_file = open("p3.txt","r")
whole_thing = text_file.read()
print("Your input are below . . .")
print(whole_thing)
