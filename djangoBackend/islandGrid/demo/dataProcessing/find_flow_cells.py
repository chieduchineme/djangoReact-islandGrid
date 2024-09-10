from collections import deque

def bfs(grid, start_points):
    # Get the number of rows (n) and columns (m) in the grid
    n, m = len(grid), len(grid[0])
    
    # Initialize a 2D list to track visited cells
    visited = [[False] * m for _ in range(n)]
    
    # Initialize a queue with the start points for BFS
    q = deque(start_points)

    while q:
        # Dequeue the front cell
        x, y = q.popleft()
        
        # Mark the cell as visited
        visited[x][y] = True
        
        # Check all four possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Calculate the new cell coordinates
            nx, ny = x + dx, y + dy
            
            # Check if the new cell is within bounds and not yet visited
            # Also, ensure the new cell's height is greater than or equal to the current cell's height
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] >= grid[x][y]:
                # Enqueue the new cell
                q.append((nx, ny))
    
    # Return the visited cells grid
    return visited

def find_flow_cells(grid):
    # Check if the grid is empty or has no columns
    if not grid or not grid[0]:
        return []

    # Get the number of rows (n) and columns (m) in the grid
    n, m = len(grid), len(grid[0])
    
    # Collect start points for BFS from the northwest and southeast boundaries
    northwest_starts = [(0, i) for i in range(m)] + [(i, 0) for i in range(1, n)]
    southeast_starts = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]

    # Perform BFS from northwest and southeast boundary points
    northwest_reach = bfs(grid, northwest_starts)
    southeast_reach = bfs(grid, southeast_starts)

    # Find cells that can flow to both northwest and southeast oceans
    result = []
    for i in range(n):
        for j in range(m):
            # Check if the cell can flow to both oceans
            if northwest_reach[i][j] and southeast_reach[i][j]:
                # Add the cell to the result list
                result.append((i, j))

    # Return the list of cells that can flow to both oceans
    return result
