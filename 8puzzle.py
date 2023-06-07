# Perform 8 puzzle problem using a* algorithm

# This function is used to calculate misplaced tiles in the puzzle which is equal to h valus
def miscount(puzzle, goalstate):
    iterate_value = 0  # Used to store count

    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle)):
            if puzzle[i][j] != '_' and puzzle[i][j] != goalstate[i][j]:
                iterate_value += 1

    return iterate_value


# This function is used to return possible direction to move the blank tile
def direction(puzzle):
    row, col = 0, 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == '_':
                row, col = i, j
                break
    directions = []
    if row > 0:
        directions.append('up')
    if row < len(puzzle) - 1:
        directions.append('down')
    if col > 0:
        directions.append('left')
    if col < len(puzzle) - 1:
        directions.append('right')
    return directions
 # [up, left, right]

# This function is used to generate the child states
def generate_child(state, direction):
    row, col = 0, 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == '_':
                row, col = i, j
                break
    new_state = [row[:] for row in state]
    if direction == 'up':
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
    elif direction == 'down':
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]
    elif direction == 'left':
        new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
    elif direction == 'right':
        new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]
    return new_state


# This function is used to compare initial state and goal state. Also return true of false value
def compare_state(i_state, g_state):
    for i in range(len(i_state)):
        for j in range(len(i_state)):
            if i_state[i][j] != g_state[i][j]:
                return False
    return True


# This function is used to display list in matrix format
def displayPuzzle(puzzle, g):
    print(f"\n-----Level {str(g)}-----")
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle)):
            print(f"{puzzle[i][j]}  ", end=' ')
        print()
    print()


# This function is used to calculate f, g, h values
def calculateValues(puzzle, goalstate, g):
    h = miscount(puzzle, goalstate)
    f = g + h
    return f, g, h


def solvepuzzle(initialState, goalState):
    # Initialize the open and closed lists
    openList = [(0, 0, initialState)]
    closedList = []
    g = 0

    while openList:
        # Get the state with the lowest f value
        openList.sort(key=lambda x: x[0])

        if not openList:
            return None

        currentF, g, currentState = openList.pop(0)

        # Display current state
        displayPuzzle(currentState, g)

        # Check if the current state is the goal state
        if compare_state(currentState, goalState):
            displayPuzzle(currentState, g)
            return currentState

        # Generate the child states
        for dir in direction(currentState):
            childState = generate_child(currentState, dir)

            if compare_state(childState, goalState):
                displayPuzzle(childState, g+1)
                return g + 1

            # Check if the child state is already in the closed list
            childG = g + 1
            childF, childG, childH = calculateValues(childState, goalState, childG)

            inClosed = False
            for closedState in closedList:
                if compare_state(childState, closedState):
                    inClosed = True
                    break

            # If the child state is not in the closed list or has a lower f value than its previous occurrence,
            # add it to the open list with its updated f and g values.
            if not inClosed:
                inOpen = False

                for i in range(len(openList)):
                    if compare_state(childState, openList[i][2]):
                        inOpen = True

                    if childF < openList[i][0]:
                        openList[i] = (childF, childG, childState)
                        break

                if not inOpen:
                    openList.append((childF, childG, childState))

        # Add the current state to the closed list
        closedList.append(currentState)

    return None


if __name__ == '__main__':
    initialState = [[3, 6, 8],[5, 1, 7],[2, 4, '_']]
    goalState =  [ [1, 2, 3], [4, 5, 6], [7, 8, '_'] ]

    result = solvepuzzle(initialState, goalState)
    if result is None:
        print("No solution found.")