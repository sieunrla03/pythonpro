choice = []
geek = {
    "404": "clueless.  From the web error message 404, meaning page not found."
}

while choice != '0':
    print("\nGeek Translator\n")
    print("0 - Quit")
    print("1 - Look Up a Geek Term")
    print("2 - Add a Geek Term")
    print("3 - Redefine a Geek Term")
    print("4 - Delete a Geek Term")
    choice = input("\nChoice: ")
    
    if choice == '0':
        print("EXIT!")
        break
    elif choice == '1':
        term = input("\nWhat term do you want me to translate?: ")
        if term in geek:
            mean = geek[term]
            print("\n", term, "means", mean)
        else:
            print("\nThis word [", term, "] does not exist.")
    elif choice == '2':
        term = input("What term do you want me to add?: ")
        if term not in geek:
            mean = input("\nWhat does it mean?: ")
            geek[term] = mean
        else:
            print("\nIt has already been added.")
    elif choice == '3':
        term = input("\nWhat term do you want me to redefine?: ")
        if term in geek:
            mean = input("What's the new definition?: ")
            geek[term] = mean
        else:
            print("\nIt doesn't exist.")
    elif choice == '4':
        term = input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print("\n", term, "is deleted")
        else:
            print("\nIt doesn't exist.")
    elif choice != '0':
        print("Please enter a valid number from the list.")

