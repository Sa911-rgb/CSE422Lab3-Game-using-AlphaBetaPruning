# A Game of attacker and defender using MinMax Algorithm and Alpha-Beta Pruning

There are two teams and they are team attacker and team defender. Therefore, at a state of the game one agent in each team is left alive respectively. Here, the defender is given a lifeline called HP which will be assigned randomly. Furthermore, the attacker agent will try to give maximum negative HP to the defender agent to decrease his(d) chances of survival in the game. On the other hand, the defender agent will try to protect himself by receiving the lowest negative HP possible from the attacker agent. Furthermore, the attacker can have a choice from a number of bullets from his gun and the optimal moves will cost a certain maximum negative HP (chosen from randomly assigned values within the range of minimum and maximum negative HP). Here, are the following things you need to do using Alpha-Beta Pruning algorithm:

Sample Input 1:

Enter your student id:

17301106

Minimum and Maximum value for the range of negative HP:

1 30

Sample Input 1 Explanation:

1. 1st digit of the bracu student id is number of turns for the attacker agent assuming that both of them will get equal number of chances
2. Last 2 digits of the bracu student id in reverse is initial lifeline (HP) for the defender at initial state of the game
3. 3rd digit of the bracu student id is number of bullets from which the final choice has to be made by the attacker.

Sample Output 1:

1. Depth and Branches ratio is 2:3
2. Terminal States (leaf node values) are 19,22,9,2,26,16,16,27,16.
3. Left life(HP) of the defender after maximum damage caused by the attacker is 44
4. After Alpha-Beta Pruning Leaf Node Comparisons 7

Note:

Terminal nodes are randomly generated values within the given range of negative HP.

Sample Input 2:

Enter your student id:

20201003

Minimum and Maximum value for the range of negative HP:

5 20

Sample Output 2:

1. Depth and Branches ratio is 4:2
2. Terminal States(Leaf Nodes) are 18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18.
3. Left life(HP) of the defender after maximum damage caused by the attacker is 22
4. After Alpha-Beta Pruning Leaf Node Comparisons 13
