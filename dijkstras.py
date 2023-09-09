from collections import deque
import os,time
import curses
import sys
def find_shortest_path(grid, start, end):
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Directions: move left or up
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    visited = set()
    queue = deque([(end, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == start:
            # Found the shortest path
            return path + [start]

        for dr, dc in directions:
            new_x, new_y = current[0] + dr, current[1] + dc
            new_pos = (new_x, new_y)
            if (
                0 <= new_x < num_rows
                and 0 <= new_y < num_cols 
                and grid[new_x][new_y] != 'O' and grid[new_x][new_y] != 'c'
                and new_pos not in visited
            ):
                if grid[new_x][new_y] == 'O' or grid[new_x][new_y] == 'c':
                    continue  # Skip 'O' and 'c' cells
                queue.append((new_pos, path + [current]))


# Example usage:
def findPaths(stdscr, grid, y, x):
    # Initialize curses settings
    curses.curs_set(0)
    stdscr.clear()

    stdscr.refresh()
    curses.napms(2000)
    stdscr.addstr(5, 5, "Generating Simulation.")
    stdscr.refresh()
    curses.napms(1000)
    stdscr.addstr(5, 5, "Generating Simulation..")
    stdscr.refresh()
    curses.napms(1000)
    stdscr.addstr(5, 5, "Generating Simulation...")
    stdscr.refresh()
    curses.napms(1000)
    stdscr.addstr(5, 5, "Generating Simulation....")
    stdscr.refresh()
    curses.napms(1000)
    carrots = []
    holes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'C':
                carrots.append([i, j])
            if grid[i][j] == 'O':
                holes.append([i, j])

    res = []
    hres = []

    for carrot in carrots:
        shortest_path = find_shortest_path(grid, (y, x), (carrot[0], carrot[1]))
        if shortest_path:
            res.append(shortest_path)

    res = sorted(res, key=lambda x: len(x))

    if not res:
        curses.endwin()
        print("Error: No valid path to any carrot.")
        sys.exit(1)

    for hole in holes:
        shortest_path = find_shortest_path(grid, (res[0][0][0], res[0][0][1]), (hole[0], hole[1]))
        if shortest_path:
            hres.append(shortest_path)

    hres = sorted(hres, key=lambda x: len(x))

    if not hres:
        curses.endwin()
        print("Error: No valid path from carrot to any rabbit hole.")
        sys.exit(1)

    r_2_c = res[0]
    r_2_c.reverse()
    e_i = 0
    e_j = 0

    for row, col in r_2_c:
        stdscr.clear()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == row and j == col:
                    stdscr.addch(i, j, ord('r'))
                    e_i = i
                    e_j = j
                else:
                    stdscr.addch(i, j, ord(grid[i][j]))
            stdscr.addstr(3, 10, " Finding Carrot")
        stdscr.refresh()
        time.sleep(1)

    c_2_o = hres[0]
    c_2_o.reverse()
    grid[e_i][e_j] = '-'

    for row, col in c_2_o:
        stdscr.clear()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == row and j == col:
                    stdscr.addch(i, j, ord('R'))
                else:
                    stdscr.addch(i, j, ord(grid[i][j]))
            stdscr.addstr(5, 10, " Finding a Rabbit hole to put that Carrot")
        stdscr.refresh()
        time.sleep(1)       
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(10, 10, "Simulation finished.")  # Indicate that the simulation has finished
    stdscr.refresh()
    time.sleep(2)
    stdscr.getch()
    
