import curses
import math

def draw_line(stdscr, start, end):
    """Draws a line from start to end points in the terminal."""
    dy = end[1] - start[1]
    dx = end[0] - start[0]
    distance = max(abs(dx), abs(dy))
    distance = math.ceil(distance)  
    for i in range(distance + 1):
        y = start[1] + i * dy / distance
        x = start[0] + i * dx / distance
        try:
            stdscr.addch(int(round(y)), int(round(x)), '*')
        except curses.error:
            pass  # Ignore errors thrown by addch for drawing outside the window

def koch_curve(stdscr, start, end, depth):
    if depth == 0:
        draw_line(stdscr, start, end)
    else:
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        dist = math.sqrt(dx ** 2 + dy ** 2) / 3
        angle = math.atan2(dy, dx)
        mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        p1 = (start[0] + dx / 3, start[1] + dy / 3)
        p2 = (mid[0] + dist * math.cos(angle - math.pi / 3), mid[1] + dist * math.sin(angle - math.pi / 3))
        p3 = (end[0] - dx / 3, end[1] - dy / 3)

        koch_curve(stdscr, start, p1, depth - 1)
        koch_curve(stdscr, p1, p2, depth - 1)
        koch_curve(stdscr, p2, p3, depth - 1)
        koch_curve(stdscr, p3, end, depth - 1)

def draw_snowflake(stdscr):
    curses.curs_set(0)  # Hide cursor
    max_y, max_x = stdscr.getmaxyx()
    center = (max_x // 2, max_y // 2)
    size = min(max_x, max_y) // 2  # Increased initial size

    points = []
    for i in range(3):
        angle = math.pi * 2 / 3 * i
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append((x, y))

    stdscr.clear()
    depth = 5  
    for i in range(3):
        koch_curve(stdscr, points[i], points[(i + 1) % 3], depth)

    stdscr.refresh()
    stdscr.getch()

def main_snowflake():
    curses.wrapper(draw_snowflake)