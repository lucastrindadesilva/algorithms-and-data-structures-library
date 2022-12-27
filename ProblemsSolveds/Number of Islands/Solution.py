from queue import Queue

class Solution:
    def numIslands(self, grid: list) -> int:
        visiteds = set()
        to_visit = Queue()
        islands = 0

        def bfs(root:tuple)->None:
            nonlocal visiteds, to_visit, islands
            
            while True:
                visiteds.add(root)
                
                x, y = root
                adjacencies = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
                for adjacency in adjacencies:
                    if (0 <= adjacency[0] < len(grid) 
                        and 0 <= adjacency[1] < len(grid[0])
                        and grid[adjacency[0]][adjacency[1]] == "1"
                        and adjacency not in visiteds):
                        
                        to_visit.put(adjacency)
                          
                if to_visit.empty():
                    islands += 1
                    break
                
                root = to_visit.get()
                    
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x,y) not in visiteds:
                    bfs(root=(x,y))
                else:
                    visiteds.add((x,y))
            

        return islands
  
s = Solution()  
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
assert s.numIslands(grid=grid), 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
assert s.numIslands(grid=grid), 3

grid = [
  ["1","0","0","0","0","0","1"],
  ["0","1","0","0","1","0","1"],
  ["1","0","1","0","1","0","0"],
  ["0","0","1","1","1","0","0"],
  ["1","0","0","1","0","0","0"],
  ["1","0","0","1","0","0","0"]
]
assert s.numIslands(grid=grid), 6