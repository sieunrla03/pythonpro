scores = []

while True:
    print("High Scores Keeper\n\n 0 - Quit\n 1 - List Scores\n 2 - Add a Score\n")

    choice = int(input("Choice:\t"))
    print()

    # 0
    if choice == 0:
        print("Good-bye!")
        break
    # 1
    elif choice == 1:
        print("High Scores")
        print("NAME\t\tSCORE")
        for player in scores:
            print(player["name"], "\t", player["score"])
    # 2
    elif choice == 2:
        name = input("What is the player's name?:\t")
        score = int(input("What score did the player get?:\t"))
        player = {"name": name, "score": score}
        scores.append(player)
        scores.sort(key=lambda x: x["score"], reverse=True)

    
    else:
        print( choice, "is invalid!")
