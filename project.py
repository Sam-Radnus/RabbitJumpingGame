import random
import sys, os
import curses
from dijkstras import findPaths
import time
def is_adjacent(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1



def generate_unique_positions(stdscr, grid, randomNums, positions_list, n, obj):
    unique_positions = []
    max_attempts = n * n  # Maximum attempts to avoid an infinite loop
    attempts = 0

    while len(unique_positions) < randomNums and attempts < max_attempts:
        position = [random.randint(1, n - 1), random.randint(1, n - 1)]
        is_valid = all(not is_adjacent(position, existing_position) for existing_position in unique_positions)
        if is_valid:
            unique_positions.append(position)
            positions_list.append(position)
            grid[position[0]][position[1]] = obj  # Place carrots or holes on the grid
        attempts += 1

    if attempts >= max_attempts:
        curses.endwin()
        print("Error: Unable to generate unique positions. Try with a smaller grid or fewer objects.")
        sys.exit(1)

    return unique_positions

def check_adj(grid, y, x, char):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dy, dx in directions:
        new_y, new_x = y + dy, x + dx
        if grid[new_y][new_x] == char:
            return True, new_y, new_x
    return False, y, x


def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(0)  # Non-blocking getch


    
    stdscr.addstr(0,0,"Enter the Grid size: ")
    stdscr.refresh()
    n = int(stdscr.getstr(0, 25, 2).decode())
    stdscr.addstr(1,0,str(n))
    grid = [['-' for _ in range(n)] for _ in range(n)]
    
    stdscr.addstr(2,0,"Enter Number of Carrots: ")
    stdscr.refresh()
    number_of_carrots = int(stdscr.getstr(0, 25, 2).decode())
    stdscr.addstr(3,0,str(number_of_carrots))
    stdscr.addstr(4,0,"Enter Number of Holes: ")
    stdscr.refresh()
    number_of_holes = int(stdscr.getstr(0, 25, 2).decode())
    stdscr.addstr(5,0,str(number_of_holes)) 
    generate_unique_positions(stdscr, grid, number_of_carrots, [], n, "C")
    generate_unique_positions(stdscr, grid, number_of_holes, [], n, "O")  # Place rabbit holes on the grid

    posX, posY, c, prevX, prevY = 0, 0, "r", 0, 0

    while True:
        stdscr.clear()
        prevX = posX
        prevY = posY
        
        dir = stdscr.getch()
        
        if dir == ord('e') and c == 'r':
            findPaths(stdscr,grid, posY, posX)
            
            break
        elif dir == ord('w'):
            posY -= 1
            posY = max(0, posY)
        elif dir == ord('d'):
            posX += 1
            posX = min(n - 1, posX)
        elif dir == ord('s'):
            posY += 1
            posY = min(n - 1, posY)
        elif dir == ord('a'):
            posX -= 1
            posX = max(0, posX)
        elif dir == ord('p') and c == "r":
            is_carrot_nearby, yPos, xPos = check_adj(grid, posY, posX, "C")
            if is_carrot_nearby:
                c = "R"
                grid[yPos][xPos] = '-'  # Remove carrot from grid
        elif dir == ord('p') and c == "R":
            is_hole_nearby, yPos, xPos = check_adj(grid, posY, posX, "O")
            if is_hole_nearby:
                stdscr.refresh()
                stdscr.getch()
                #time.sleep(2)
                
                #time.sleep(2)
                curses.endwin()
                print("Congratulations! You have won!\n")
                sys.exit()
                
        elif dir == ord('j'):
            is_hole_nearby, yPos, xPos = check_adj(grid, posY, posX, "O")
            if is_hole_nearby:
                tempX = xPos - posX
                tempY = yPos - posY
                posX += 2 * tempX
                posY += 2 * tempY

            if posX < 0 or posY < 0 or posX >= len(grid[0]) or posY >= len(grid):
                posX = prevX
                posY = prevY

        elif dir == ord('-'):
            curses.endwin()
            sys.exit()

        if grid[posY][posX] == 'C' or grid[posY][posX] == 'O':
            posX = prevX
            posY = prevY

        # Print the updated grid
        
        
        # Print the grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == posY and j == posX:
                    stdscr.addch(posY, posX, ord(c))
                else:
                    stdscr.addch(i, j, ord(grid[i][j]))
                
        
        # Refresh the screen
        stdscr.refresh()
        time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(main)
