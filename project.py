import random
import sys,os

def is_adjacent(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def intro():
    print("--------------------------------------------------------------")
    print("         Welcome to the Rabbit's Carrot Quest Game!")
    print("--------------------------------------------------------------\n")
    
    print("Instructions:")
    print("- Use the arrow keys to guide Mr. Bunny through the garden.")
    print("- Press 'w' to move upward")
    print("- Press 's' to move downward")
    print("- Press 'a' to move left")
    print("- Press 'd' to move right")
    print("- Press 'p' to pick up a carrot when next to it")
    print("- Press 'j' to jump over rabbit holes")
    print("- Press 'E' to start simulation")
    print("- Collect carrots and drop them into the rabbit holes to win!")
    print("- Be careful not to get stuck or fall into holes!\n")
    
    print("Gameplay:")
    print("- Mr. Bunny starts with 'r' and can pick up carrots ('c') to become 'R'.")
    print("- Once 'R', he can drop carrots in rabbit holes ('O') to win.")
    print("- Collect all carrots, deposit them, and you're victorious!")
    print("- Press '-1' anytime to exit the game.\n")
    
    print("Have fun helping Mr. Bunny gather carrots and enjoy the adventure!")
    print("--------------------------------------------------------------")

def generate_simulation(grid):
    pass

def generate_unique_positions(randomNums, positions_list, n):
    unique_positions = []
    while len(unique_positions) < randomNums:
        position = [random.randint(1, n - 1), random.randint(1, n - 1)]
        is_valid = all(not is_adjacent(position, existing_position) for existing_position in unique_positions)
        if is_valid:
            unique_positions.append(position)
            positions_list.append(position)
    return unique_positions

def check_adj(grid, y, x, char, lists):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dy, dx in directions:
        new_y, new_x = y + dy, x + dx
        if [new_y, new_x] in lists:
            return True, new_y, new_x
    return False, y, x

def main():
    intro()
    n = int(input("Enter grid size: "))
    grid = [['-' for _ in range(n)] for _ in range(n)]
    number_of_carrots = int(input("Enter Number of Carrots: "))
    number_of_holes = int(input("Enter Number of Holes: "))
    carrots = []
    holes = []

    generate_unique_positions(number_of_carrots, carrots, n)
    generate_unique_positions(number_of_holes, holes, n)

    posX, posY, c, prevX, prevY = 0, 0, "r", 0, 0

    while True:
        printGrid(grid,posX,posY,c,carrots,holes)
        prevX = posX
        prevY = posY
        
        dir = input("Enter your Instruction")[0]
        os.system('cls')
        if dir=="e" or dir=="E":
            generate_simulation(grid)
        elif dir == "w":
            posY -= 1
            posY = max(0, posY)
        elif dir == "d":
            posX += 1
            posX = min(n-1, posX)
        elif dir == "s":
            posY += 1
            posY = min(n-1, posY)
        elif dir == "a":
            posX -= 1
            posX = max(0, posX)
        elif dir == "p" and c == "r":
            is_carrot_nearby, yPos, xPos = check_adj(grid, posY, posX, "c", carrots)
            if is_carrot_nearby:
                c = "R"
                carrots.remove([yPos, xPos])
        elif dir == "p" and c == "R":
            is_hole_nearby, yPos, xPos = check_adj(grid, posY, posX, "O", holes)
            if is_hole_nearby:
                print("Congratulations! You have won!")
                sys.exit()
        elif dir == "j":
            is_hole_nearby, yPos, xPos = check_adj(grid, posY, posX, "O", holes)
            if is_hole_nearby:
                tempX = xPos - posX
                tempY = yPos - posY
                posX += 2 * tempX
                posY += 2 * tempY

            if posX < 0 or posY < 0 or posX >= len(grid[0]) or posY >= len(grid):
                posX = prevX
                posY = prevY
        else:
            break

        if [posY, posX] in carrots or [posY, posX] in holes:
            posX = prevX
            posY = prevY

        

def printGrid(grid,posX,posY,c,carrots,holes):
    for i in range(len(grid)):
            print()
            for j in range(len(grid[i])):
                if i == posY and j == posX:
                    print(c + " ", end="")
                elif [i, j] in carrots:
                    print("c" + " ", end="")
                elif [i, j] in holes:
                    print("O" + " ", end="")
                else:
                    print(grid[i][j] + " ", end="")
            print()
        
    



if __name__ == "__main__":
    main()
