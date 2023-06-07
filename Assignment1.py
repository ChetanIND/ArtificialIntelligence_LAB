# BFS Algorithm
list = {0: [], 1:[], 2: [], 3:[]}

class Graph:
    def __init__(self):
        self.grapht = list
        
    def addEdge(self, u, v):
        self.grapht[u].append(v)
        
    def bfs(self, s):
        visits = [False] * (max(self.grapht) + 1)
        
        queue = []
        queue.append(s)
        visits[s] = True
        
        while queue:
            s = queue.pop(0)
            print(f"{s} ")
            
            for i in self.grapht[s]:
                if visits[i] == False:
                    queue.append(i)
                    visits[i] = True

# DFS Algorithm
listm = {0: [], 1:[], 2: [], 3:[]}

class Graphm:
    def __init__(self):
        self.grapht = listm
        
    def addEdgem(self, u, v):
        self.grapht[u].append(v)
        
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)
 
        for neighbour in self.grapht[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    def dfs(self, s):
        visited = set()
 
        self.DFSUtil(s, visited)

# DLS Algorithm
listg = {'A': [], 'B':[], 'C': [], 'D':[],'E': [], 'F':[], 'G': [], 'H':[],'I':[]}

class Graphg: 
    def __init__(self): 
    # setting the data member adj_list as an empty dictionary 
        self.adj_list = listg 
        
    def addEdgeg( self, node1, node2 ): 
        # adding a edge from node1 to node2 
        self.flag = False 
        self.adj_list [node1].append(node2); 
        
    def dlsUtil( self, node, visited, goal, height, limit ): 
        # checking if the node is required node or not 
        if( node == goal ): 
            self.flag = True 
            print("Node Found", node ) 
            return 
        # else checking if height is greater that or equal to the height limit 
        elif(height >= limit ): 
            return 
        visited.add(node) 
        
        # executing depth first search for all unvisited neighbours of the current node 
        for neighbour in self.adj_list[node]: 
            if neighbour not in visited: 
                self.dlsUtil( neighbour, visited, goal, height+1, limit)
            
    def DLS(self, v ): 
        # setting the visited as a set of bool values 
        visited = set() 
        # getting the node to search from the user 
        goal_node = input("Enter the goal node: ") 
        # getting the limit from 
        
        limit = int(input("Enter the limit : "))
        
        if( limit == 0 ): 
            print("Cannot search with a limit of 0") 
            return 
        
        # starting height would be 0 
        start_height = 0 
        self.dlsUtil( v, visited, goal_node, 0, limit) 
        
        # checking using a data member flag if the node was found or not 
        if( not self.flag ): 
            print("Node is not present", goal_node ) 

if __name__ == "__main__":
    # BFS Algorithm
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("BFS Algorithm Output: ")
    g.bfs(2)

    # DFS Algorithm
    g = Graphm()
    g.addEdgem(0, 1)
    g.addEdgem(0, 2)
    g.addEdgem(1, 2)
    g.addEdgem(2, 0)
    g.addEdgem(2, 3)
    g.addEdgem(3, 3)
    print("DFS Algorithm Output: ")
    g.dfs(2)

    # DLS Algorithm
    # creating object of class Graph 
    g = Graphg()   

    # adding edges to graph 
    g.addEdgeg('A', 'B') 
    g.addEdgeg('A', 'C') 
    g.addEdgeg( 'B', 'D' ) 
    g.addEdgeg( 'B', 'E' ) 
    g.addEdgeg( 'C', 'F' ) 
    g.addEdgeg( 'C', 'G' ) 
    g.addEdgeg( 'F', 'H' ) 
    g.addEdgeg( 'F', 'I' ) 
    g.addEdgeg( 'H', 'J' ) 
    g.addEdgeg( 'H', 'K' ) 
    g.addEdgeg( 'I', 'L' ) 
    g.addEdgeg( 'I', 'M' ) 

    print("DLS Algorithm Output: ") 
    # calling the function 
    g.DLS( 'A' ) 

