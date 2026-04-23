Leaderboard = {}

while True:
    print("\n1. Add Score: \n2. Show Leaderboard: \n3. Check Rank: \n4. Exit: ")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Start Adding Player Name and Score")
        Player_Name = input("Enter Player Name: ")
        Score = int(input("Enter Your Score: "))
        if Player_Name in Leaderboard:
            print("Player name already present in dictionary")
            Leaderboard[Player_Name]["Score"] += Score
        else:
            Leaderboard[Player_Name] = {"Score" : Score}
            print(Leaderboard)
            print("Score updated")
    elif choice == "2":
        if Leaderboard:
            print("Show Leaderboard")
            Sort_Board = sorted(Leaderboard.items(), key=lambda x: x[1]["Score"], reverse= True)
            rank = 1
            print(Sort_Board)
            for name, data in Sort_Board:
                print(f"{rank}: {name}- {data["Score"]} points")
                rank += 1
        else:
            print("Leaderboard is Empty")
    elif choice == "3":
        player_name = input("Enter the Player name: ")
        Sort_Board = sorted(Leaderboard.items(), key= lambda x: x[1]["Score"], reverse= True)
        rank = 1       
        found = False
        for name, data in Sort_Board:
            if player_name == name:
                print(f"player name found with Rank {rank}")
                found =True
            rank += 1
        if not found:
            print("Player name not found")
    elif choice == "4":
        print("Want to exit")
        break
    else:
        print("invalid input, try with different number ")
            

