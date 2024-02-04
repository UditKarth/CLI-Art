import curses
import random
import time

def draw_rain(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input
    max_y, max_x = stdscr.getmaxyx()  # Get screen size
    raindrops = []  # List to store raindrops

    while True:
        # Handle key press
        key = stdscr.getch()
        if key == ord('q'):
            break

        # Add a new raindrop at a random position and speed
        if len(raindrops) < 100:  # Limit the number of raindrops
            raindrops.append([0, random.randint(1, max_x-2), random.uniform(0.1, 0.5)])

        stdscr.clear()  # Clear the screen

        new_raindrops = []
        for drop in raindrops:
            new_y = drop[0] + drop[2]  # Update the y position based on speed
            if new_y < max_y - 1:
                new_raindrops.append([new_y, drop[1], drop[2]])
                stdscr.addstr(int(new_y), drop[1], '*')
        
        raindrops = new_raindrops

        stdscr.refresh()  # Refresh the screen
        time.sleep(0.05)  # Control the animation speed

def main_rain():
    curses.wrapper(draw_rain)