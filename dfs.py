import time
import sys
sys.setrecursionlimit(10000)

# Question 1.2


def dfs(maze, start, goal, visited=None):
    if visited is None:
        visited = set()
        # Start gets added assigned to the value of current
    current = start
        # Current node gets added to the visited set
    visited.add(current)
        # Checking if the end is met 
    if start == goal:
        return [current]
    row, col = current
    # All moves from the current location
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)): 
        r, c = row + dr, col + dc
        # Checking if moves are possible 
        if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]) or maze[r][c] == 1 or (r, c) in visited:
            continue
        path = dfs(maze, (r, c), goal, visited)
        if path is not None:
            #print("Total nodes visited ", len(visited))
            return [current] + path
        
    return None
    



def main():
    # Takes an imputted filename and coverts it into a 1 and 0 maze form
    filename = input("Enter the name of your file ")
    with open(filename) as f:
                contents = f.read()
                maze = contents.replace('#','1').replace('-', '0')
                maze = [[int(i) for i in line.split()] for line in maze.split('\n')]


# Finds the start and end location of the inputted maze
    for i in range(len(maze[0])):
            if maze[0][i] == 0:
                start = (0,i)
            
    for i in range(len(maze[0])):
            if maze[len(maze)-1][i] == 0:
                goal = (len(maze)-1,i)


    start_time = time.time()         
    path = dfs(maze, start, goal)
    print("--- %s seconds ---" % (time.time() - start_time))
    # Time import used either side of the function call to time just the algorithm speed
    print("The length of the chose path: ", len(path),"And the shorest path: ", path)



if __name__ == "__main__":
    main()
    




