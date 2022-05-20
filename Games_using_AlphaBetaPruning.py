import random

id = input("1. Enter your student id:\n")
r = input("2. Minimum and Maximum value for the range of negative HP:\n")
#Multiply the first digit of id by 2 to find the depth
depth = int(id[0])*2
#Initial HP of the  defender
hp = int(id[:-3:-1])
#Branching factor of the tree or the number of bullets from which the first choice will be made
branch = int(id[2])
#minimum and maximum values of range
mn = int(r.split()[0])
mx = int(r.split()[1])
#Counter for keeping track of the pruned leaves
comp = 0
#Randomly generated leaf nodes between the given range
bullets = [random.randint(mn, mx) for _ in range(1, pow(branch, depth)+1)]
#bullets = [19, 22, 9, 2, 26, 16, 16, 27, 16]
#bullets = [18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18]

def minimax(leafs, depth, a, b, index, maximizingPlayer):
    global comp
    #Check if a terminal state or a leaf node has been reached
    if depth == 0:
        comp += 1
        return leafs[index]
    #Max level
    if maximizingPlayer:
        maxEval = float('-inf')
        
        for i in range(0, branch):
            eval = minimax(leafs, depth-1, a, b, index * branch + i, False)
            maxEval = max(maxEval, eval)
            a = max(a, eval)
            #Alpha-Beta Pruning
            if b <= a:
                break
        return maxEval
    #Min level
    else:
        minEval = float('inf')
        
        for i in range(0, branch):
            eval = minimax(leafs, depth-1, a, b, index * branch + i, True)
            minEval = min(minEval, eval)
            b = min(b, eval)
            #Alpha-Beta Pruning
            if b <= a:
                break
        return minEval

#Left HP of the  defender
hp = hp - minimax(bullets, depth, float('-inf'), float('inf'), 0, True)
#Make a string with the elements of the bullets list
ts = (','.join(map(str, bullets)))

print("1. Depth and Branches ratio is {d}:{b}".format(d = depth, b = branch), "2. Terminal States(Leaf Nodes) are {}.".format(ts), "3. Left life(HP) of the defender after maximum damage caused by the attacker is {}".format(hp), "4. After Alpha-Beta Pruning Leaf Node Comparisons {}".format(comp), sep='\n')