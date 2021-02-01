import utils


# General Search Algorithm(will act as different search algoritm according to the
# frontier pass in as argument)
def generalSearch(problem, frontier, heuristics = utils.manhattanDistance):
    seen = set()
    history = []

    start = problem.getStartState()
    if isinstance(frontier, utils.PriorityQueue):
        p = utils.manhattanDistance(problem.getStartState(), problem.getGoal())
        frontier.push((start, [start]), p)
    else:
        frontier.push((start, [start]))

    while frontier:
        problem.incrementIter()

        currentNode, path = frontier.pop() 
        # expanded.append(currentNode)

        if currentNode not in seen:
            seen.add(currentNode)

            #  check if we reached the goal
            if problem.isGoal(currentNode):
                history.append((currentNode, seen.copy(), []))
                return path, history

            # else expand this node
            else:
                discovered =  problem.getSuccessors(currentNode)
                for child in discovered:
                    # history  for visualization
                    history.append((currentNode, seen.copy(), discovered))

                    if isinstance(frontier, utils.PriorityQueue):
                        p = heuristics(child, problem.getGoal())

                        #print("from: " + str(child) + " Distance: " + str(p))

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
def astar(problem, heuristic=utils.manhattanDistance):
    return generalSearch(problem, utils.PriorityQueue(), heuristic)


# uniform cost Search
# this is same as astart except its heuristic will always return 0
def ucs(problem):
    return astar(problem, utils.nullHeuristic)



