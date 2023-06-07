# The below function returns the neighbor nodes to a node in a graph.
# It takes two positional parameters: 'graph' and 'x'.
def get_neighbournodes(graph, x):
    # Checks for the presence of node 'x' in the graph.
    if x in graph:
        return graph[x]  # Returns all neighbors of node 'x', which are part of the graph.
    else:
        print('Empty')  # If the node does not exist in the graph, then it displays 'Empty'.

# This function assigns heuristic values to each node of the given graph. It takes one positional parameter: 'x'.
def heuristic_val(x):
    # This is a dictionary that contains heuristic values.
    h_values = {'S': 14, 'B': 12, 'C': 11, 'D': 7, 'E': 9, 'F': 0, 'G': 10}

    # This returns the heuristic value of a given node 'x', based on the dictionary 'h_values'.
    return h_values[x]

# This is an implementation of the A* algorithm. It takes three positional parameters: 'graph', 'startnode', and 'stopnode'.
def astar_algo(graph, startnode, stopnode):
    # It checks whether the 'startnode' and 'stopnode' exist within the given 'graph'. If not, then it will display "Start or stop node not found in graph."
    if startnode not in graph or stopnode not in graph:
        print("Start or stop node not found in graph.")
        return None
    
    #The openlist contains nodes that need to be explored / traversed further to find the shortest path from startnode to stopnode. 
    #The closelist contains nodes which have already been traversed.
    openlist = {startnode}  # Initiate an empty set with the 'startnode' as the first element.
    closelist = set()  # Initiate another empty set.

    g = {}  # A dictionary to store distance between the 'startnode' and the current node.
    parent = {}  # A dictionary containing which node the current node came from during the traversal.

    g[startnode] = 0  # Distance of 'startnode' itself from 'startnode' is equal to 0.
    parent[startnode] = startnode  # Parent of start node is also itself.

    while len(openlist) > 0:
        temp = None  # Assigning temporary variable to None.

        for x in openlist:  # For each node 'x' present in the open list, perform these operations:

            # Compares the current 'temp' value with the f(n) value of node 'x'.
            # Returns the lower of the two.
            if temp is None or g[x] + heuristic_val(x) < g[temp] + heuristic_val(temp):
                temp = x  # Sets the value of 'temp' to the lower of the two.

        if temp == stopnode:  # If 'temp' is equal to the 'stopnode', calculate the path taken and return it.
            path = []

            while parent[temp] != temp:  # Traverse the 'parent' dictionary until we reach the starting node.
                # Append the current node to the 'path' list.
                path.append(temp)
                temp = parent[temp]
            path.append(startnode)  # Append 'startnode' to the end of the path list.
            path.reverse()  # Reverse the list since we started from the end.
            print(f"Path = {path}")  # Display the path on the console.
            return path

        elif graph[temp] is None:  # If the neighbor of 'temp' node has no value, then move onto the next node.
            pass

        else:  # If the above conditions do not hold true, continue with calculating the shortest path.

            # Calculate distance between the 'startnode' and the 'm' node present in the neighbor nodes of 'temp'.
            for (m, wgh) in get_neighbournodes(graph, temp):
                # Searching in both the 'openlist' and 'closelist'.
                
                if m not in openlist and m not in closelist:
                    openlist.add(m)   # Add the node to the 'openlist'.
                    parent[m] = temp   # Assign the current node 'temp' as the parent of the node 'm'.
                    g[m] = g[temp] + wgh  # Add the previous value of node g(m) to the weight of the current node.

                else:

                    if g[m] < g[temp] + wgh:  # If previously calculated distance is less than the new one, replace it with the new distance.
                        g[m] = g[temp] + wgh
                        parent[m] = temp

                        if m in closelist:
                            closelist.remove(m)
                            openlist.add(m)
                             
            openlist.remove(temp)
            closelist.add(temp)

        if temp is None:
            print("Path does not exist")
            return None
            
    print("Path does not exist!")
    return None

if __name__ == "__main__":                
    graph = {'S':[('B', 4), ('C', 3)],
            'B':[('D', 2), ('E', 5)],
            'D':['F', 1],
            'C':[('G', 1), ('E', 2)],
            'E':['F', 3],
            'G':['E', 2]
            }

    astar_algo(graph, 'S', 'G') 
