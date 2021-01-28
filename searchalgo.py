import utils


# General Search Algorithm(will act as different search algoritm according to the
# frontier pass in as argument)
def generalSearch(problem, frontier):
    seen = []
    expanded = []

    frontier.push((problem.getStartState(), []))

    while frontier:
        currentNode, path = frontier.pop() 

        if currentNode not in seen:
            seen.append(currentNode)
            #  check if we reached the goal
            if problem.isGoal(currentNode):
                return path, expanded
            
            # else expand this node
            else:
                for child in problem.getSuccessors(currentNode):
                    expanded.append(child)
                    if isinstance(frontier, utils.PriorityQueue):
                        p = utils.manhattanDistance(child, problem.getGoal())
                        frontier.push((child, path + [child]), p)
                    else:
                        frontier.push((child, path + [child]))

    # Should never get here for valid grid
    return [],[]         


# Depth First Search
def dfs(problem):
    return generalSearch(problem, utils.Stack())


# Breadth First Search
def bfs(problem):
    return generalSearch(problem, utils.Queue())

# astar search(default heuristic is null heuristic)
def astar(problem, heuristic=utils.nullHeuristic):
    return generalSearch(problem, utils.PriorityQueue(heuristic))


# uniform cost Search
# this is same as astart except its heuristic will always return 0
def ucs():
    pass



