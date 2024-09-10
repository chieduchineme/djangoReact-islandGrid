# GENERAL APPROACH

A. Understanding Water Flow Dynamics
Northwest Edge: Water flows from a higher or equal elevation to a lower elevation and can potentially reach the northwest ocean if it starts from the northwest corner (cells in the first row or first column).
Southeast Edge: Similarly, water can reach the southeast ocean if it can flow to the southeast corner (cells in the last row or last column).
We need to calculate how many cells can flow to both edges.

B. Steps to Solve the Problem
Step 1: Read the Data from Google Sheets
For each "case" (sheet), we will load the grid data representing the topography of the island.

Step 2: Algorithm Development
We’ll use a depth-first search (DFS) or breadth-first search (BFS) to find which cells can reach both the northwest and southeast edges.

Northwest DFS/BFS:
Start from all the cells in the first row and first column.
Traverse through the grid following the rule that water can flow from a higher or equal elevation to lower elevation cells.
Mark all reachable cells.

Southeast DFS/BFS:
Start from all the cells in the last row and last column.
Traverse through the grid using the same flow rule, marking all reachable cells.

Intersection:
After the above two traversals, the cells marked by both the northwest and southeast DFS/BFS can flow to both oceans.

Implemented via code:
- bfs function: This performs a BFS from a set of starting points, marking all reachable cells where water can flow.
- find_flow_cells function: It runs the BFS twice, once for northwest starting points and once for southeast starting points. The intersection of the two reachable areas gives the cells that can flow to both oceans.

# Reason for BFS AHEAD OF DFS

1. Level-by-Level Exploration:
BFS explores nodes level-by-level, which is useful when you want to propagate information through a grid in a manner that respects the relative distances from the starting points. For this problem, it means that BFS will systematically explore all cells that are reachable in each "layer" of the grid starting from the boundary cells.

DFS, on the other hand, dives deep into one path before backtracking, which can be less efficient for this kind of problem where you need to ensure that you explore all possible paths in a more evenly distributed manner.

2. Handling of Height Constraints:
In the BFS approach, the grid is processed such that only cells that have a height equal to or greater than the current cell are visited. This aligns well with the problem's requirement that water can only flow from higher or equally high cells to lower or equally low cells.

DFS can also handle height constraints, but maintaining a consistent state of which cells have been processed and managing stack depth can become complex and less efficient, especially in large grids.

3. Avoiding Deep Recursion:
DFS can lead to deep recursion, especially in large grids or complex terrains. This may lead to stack overflow issues if the recursion depth exceeds the limit.

BFS uses an iterative approach with a queue, which avoids deep recursion and is generally more memory-efficient for this type of grid traversal problem.

4. Uniform Exploration:
BFS ensures that all reachable cells from the starting points are processed in a uniform manner, guaranteeing that cells reachable from multiple starting points are identified correctly.

DFS might not uniformly explore all possible paths from a given start point and can lead to inefficient processing or incomplete exploration if not carefully managed.

5. Natural Fit for Multi-Source Problems:
In this problem, you need to perform BFS from multiple starting points (the boundaries of the grid). BFS handles this scenario naturally by initializing the queue with all starting points, while DFS would require additional handling to efficiently manage multiple starting points.

# Step 3: Output the Results
For each grid, output the number of cells that can flow to both oceans and their coordinates.
Create a web interface where users can select the scenario (sheet) and view the results.

# To always get a refresh_token, authenticate_and_get_credentials() function includes access_type='offline' and prompt='consent'. This will force Google to provide a refresh_token even if the (same) user has previously granted access.


