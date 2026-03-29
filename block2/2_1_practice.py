# Task: Use if, elif, else with nested conditions.

choice = input("You're in a dungeon. Your options are (call for help, explore, or rest): ").strip().lower()

if choice == "call for help":
    print("You shout for help, a hungry roar answers in the distance. You hear the sound of wreckless crashing and the roar getting closer.")
elif choice == "explore":
    print("You find a hidden door and escape the dungeon. You're free!")
elif choice == "rest":
    print("You take a rest, but are attacked by monsters and lose.")
else:
    print("Invalid choice. You hesitate and the dungeon's dangers catch you off guard. You lose.")