import curses
import random
import time
import math

def generate_initial_dunes(max_x, max_height=8, frequency=0.05):
    """Generates initial dune shapes using a sine wave."""
    dunes = [int((math.sin(x * frequency) + 1) / 2 * max_height) + max_height // 4 for x in range(max_x)]
    return dunes

def draw_dunes(stdscr, dunes):
    max_y, max_x = stdscr.getmaxyx()
    for x, height in enumerate(dunes):
        for y in range(max_y - height, max_y):
            try:
                stdscr.addch(y, x, random.choice(['~', '`', '"', "'"]))
            except curses.error:
                pass

def update_dunes(dunes, max_height=5):
    for i in range(len(dunes)):
        change = random.choice([-1, 1])  # Change in height
        dunes[i] = max(1, min(max_height, dunes[i] + change))  # Ensure within bounds

def main_dunes(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    max_y, max_x = stdscr.getmaxyx()

    dunes = generate_initial_dunes(max_x)

    while True:
        stdscr.clear()
        draw_dunes(stdscr, dunes)
        stdscr.refresh()

        # Randomly update dunes to simulate shifting
        if random.random() < 0.1:  # Adjust probability as needed
            update_dunes(dunes)

        # Refresh animation at random intervals
        time.sleep(random.uniform(0.1, 0.5))  # Adjust timing as needed

        key = stdscr.getch()
        if key == ord('q'):
            break