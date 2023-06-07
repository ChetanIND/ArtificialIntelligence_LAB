# import random 
# def generate value
# def generate random solution 
# def hill climbing 
# def evaluation 
# def print solution

map = {
'pune':[('ahmednagar',180), ('nagpur',270)],
'nagpur': [('ahmednagar',56), ('nashik',69), ('ranjangao',55)],
'nashik': [('nagpur',80)],
'beed': [('aurangabad',78)],
'ranjangao': [('aurangabad',82)],
'ahmednagar':[('beed',400)],
'aurangabad': 0
}

def neighbour( graph, pos ):
    return graph[pos]

def hill_climbing( graph, pos, total_dist, close_list ):
    # appending the current position in the closed list
    close_list.append( pos )
    # if current position is goal position then printing the path
    # and exiting
    if( graph[pos] == 0 ):
        print("Total distance is :", total_dist )
        print("Path is :", close_list )
        return True
    else:
    # getting all neighbours from current position
        n = neighbour( graph, pos )
        distance = 2000
        # iterating
        for loc, dist in n:
            if( distance > dist ):
                distance = dist
                next_loc = loc
                total_dist += distance
                # if destination is found then clearing next positions and returning
            if( hill_climbing( graph, next_loc, total_dist,close_list ) ):
                n.clear()
                return True
            return False

close_list = []

hill_climbing( map, 'pune', 0, close_list )
