from collections import deque
import os,time
def find_shortest_path(grid,start,end):
    

    num_rows = len(grid)
    num_cols = len(grid[0])

    # Find the positions of 'R' and 'C'
    print(start)
    print(end)
    if start is None or end is None:
        return None  # If either 'R' or 'C' is not found, there's no valid path

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
                and grid[new_y][new_x]!='O' and grid[new_y][new_x]!='C'
                and new_pos not in visited
            ):
                queue.append((new_pos, path + [current]))

    return None

# Example usage:
def findPaths(grid,y,x):
    carrots=[]
    holes=[]
    for i in range(len(grid)):
        print()
        for j in range(len(grid[0])):
            if grid[i][j]=='C':
                carrots.append([i,j])
            if grid[i][j]=='O':
                holes.append([i,j])
            if i == y and j == x:
                print("r" + " ", end="")
            else:
                print(grid[i][j] + " ", end="")
        print()
    #print(carrots)
    res=[]
    hres=[]
    for carrot in carrots:
        shortest_path = find_shortest_path(grid,(y,x),(carrot[0],carrot[1]))
        #print(shortest_path)
        if shortest_path:
            res.append(shortest_path)
    res=sorted(res,key= lambda x:len(x))    
    #print()
    #print(holes)
    #print(res)
    #print()
    #print(res[0][0][0],res[0][0][1])
    for hole in holes:
        shortest_path = find_shortest_path(grid,(res[0][0][0],res[0][0][1]),(hole[0],hole[1]))
        #print(shortest_path)
        if shortest_path:
           hres.append(shortest_path)
    hres=sorted(hres,key=lambda x:len(x))

    print(res[0])
    
    print(hres[0])
    
    print(res[0][0][0],res[0][0][1])
    
    print(hres[0][0][0],hres[0][0][1])
    r_2_c=res[0]
    r_2_c.reverse()
    for row,col in r_2_c:
        os.system('cls')
        for i in range(len(grid)):
            print()
            for j in range(len(grid[0])):
                if i==row and j==col:
                    print("r"+" ",end="")
                else:
                    print(grid[i][j]+" ",end="")
            print()
        time.sleep(2)
    c_2_o=hres[0]
    c_2_o.reverse()
    for row,col in c_2_o:
        os.system('cls')
        for i in range(len(grid)):
            print()
            for j in range(len(grid[0])):
                if i==row and j==col:
                    print("R"+" ",end="")
                else:
                    print(grid[i][j]+" ",end="")
            print()
        time.sleep(2)
    print(y,x) 
    print(res)
    print(hres)
        
   
    
