def show_menu():
    print("\n--- Leaderboard Tracker ---")
    print("1. Add Player Score")
    print("2. Show Leaderboard")
    print("3. Exit")

def add_score():
    name = input("Enter player name: ")
    score = input("Enter score: ")

    with open("leaderboard.txt", "a") as file:
        file.write(name + "," + score + "\n")
    print("Score added!")

def show_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            lines = file.readlines()
            
            players = []

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    name = parts[0]
                    score = int(parts[1])
                    players.append((name, score))
            
            # Sort by score in descending order
            players.sort(key=lambda x: x[1], reverse=True)

            print("\n--- Leaderboard ---")
            for i, (name, score) in enumerate(players, start=1):
                print(f"{i}. {name} - {score}")
    except FileNotFoundError:
        print("No scores yet.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_score()
    elif choice == "2":
        show_leaderboard()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice. Try again.")