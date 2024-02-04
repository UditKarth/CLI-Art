from raindrop import main_rain
from snowflake import main_snowflake
from sand_dunes import main_dunes
import curses
def main():
    # Figure out what the user wants to draw
    print("What would you like to draw?")
    print("1. Raindrops")
    print("2. A snowflake")
    print("3. Sand dunes")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        main_rain()
    elif choice == '2':
        main_snowflake()
    elif choice == '3':
         curses.wrapper(main_dunes)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
