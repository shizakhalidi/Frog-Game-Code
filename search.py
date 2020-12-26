# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import operator

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
       
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        util.raiseNotDefined()


def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    current_state = problem.getStartState() #the first state is the current_state
    #print(current_state)
    actions=[]
    prior_path=[]
    closed_list=[]
    open_list=[]
    while problem.isGoalState(current_state) != True: #while current_state is not the goal state
        closed_list.append(current_state)  # add current_state to closed list as it has been visited
        successor_list=problem.getSuccessors(current_state) # get all successors of current state; this will be the successor list
        prior_path.append(current_state)
        
        for i in successor_list: # traverse through successor list

            
            h=problem.getHeuristic(i[0]) #get heuristic of successor 
            actions.append(i[1]) # add the action needed for successor into actions list
            g=problem.getCostOfActions(actions)  #get cost of the entire action list from start to successor
            f=h+g  # heursitic + action is the evaluating function
            actions_2=actions[:]
            prior_path.append(i[0])

            prior_path2=prior_path[:]
            del prior_path[-1]
            del prior_path2[-1]
            
            entry=[f,i[0],actions_2,prior_path2] # the function value, successor state, list of actions and prior path are added to the entry of the successor
            del actions[-1]  
            if entry[1] not in closed_list:   #entry added to open list if the successor state hasnt been already used
                open_list.insert(0,entry) 
                
        open_list=sorted(open_list, key=operator.itemgetter(0)) #sorting open list based on function value
        current_state = open_list[0][1] #current state becomes state with least function value
        actions=open_list[0][2]
        prior_path= open_list[0][3]
        f_2=open_list[0][0] 
        del open_list[0]  #the current state is removed from open list
        
        #print("f val of above:",f_2)
    prior_path.append(current_state) #prior path is the path you should take to reach goal state from start state
    for x in prior_path:
        print(x)
    
    return prior_path
        
    
    #return closed_list

    






