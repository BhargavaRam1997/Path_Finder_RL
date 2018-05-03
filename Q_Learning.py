import random
#def epsilon_greedy(state, epsilon, p_actions):
 #   if random.uniform(0,1) < epsilon:
  #      return p_actions[random.randrange(len(possible_actions))]
   # else: #takes list of actions,lambda function finds action with max value
    #    return -1
R=[[-1,-1,-1,-1,0,-1],
    [-1,-1,-1,0,-1,100],
    [-1,-1,-1,0,-1,-1],
    [-1,0,0,-1,0,-1],
    [0,-1,-1,0,-1,100],
    [-1,0,-1,-1,0,100]]
    
Q=[[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]
    
Episodes=[0,1,2,3,4,5]
Goal=5;
done='N';
possible_actions=[]
next_possible_actions=[]
possible_Q=[]
Gamma=0.8
epsilon = 0.017
while done=='N':
    
    Current_State=Episodes[random.randrange(len(Episodes))]
    #Current_State=1;
    #print(Current_State)
    while Current_State!=Goal:
        print("Current State is: ", Current_State)
        for i in range(0,6):
            if R[Current_State][i]!=-1:
                possible_actions.append(i)
            i=i+1;
        action=possible_actions[random.randrange(len(possible_actions))]
        #action=5
        #action=epsilon_greedy(Current_State, epsilon, possible_actions)
       # if action==-1:
         #   maxi=-1
          #  for i in range(len(possible_actions)):
           #     if R[Current_State][possible_actions[i]]>maxi:
            #        maxi=R[Current_State][possible_actions[i]]
             #       action=possible_actions[i]
              #  i=i+1
                                    
        #print("Action Choosed is: ")
        #print(action);
        Next_State=action;
    
        for i in range(0,6):
            if R[action][i]!=-1:
                next_possible_actions.append(i)
            i=i+1;
            
        for i in range(len(next_possible_actions)):
            possible_Q.append(Q[action][next_possible_actions[i]])
            i=i+1


            
        #print(max(possible_Q))

            
        Q[Current_State][action]=R[Current_State][action]+(Gamma)*(max(possible_Q));
        print(Q)
        #print(Q[Current_State][action])
        #for i in range(0,6):
         #   for j in range(0,6):
          #      print(Q[i][j])
           #     j=j+1
            #print
            #i=i+1
        #print

        Current_State=Next_State;
        possible_actions.clear();
        next_possible_actions.clear();
        possible_Q.clear();
        
        #for i in range(0,6):
            
         #   for j in range(0,6):
          #      print(Q[i][j])
           #     j=j+1
            
            #i=i+1
    print("Enter done : Y/N")
    done=input()
   
    
#print "Finish"
done='N'
while done=='N':
    x=int(input("Enter initial state: "))   
    while x!=5:
        print(x, " -------> ", end=" " )
        maximum=-1
        pos=-1
        for i in range(0,6):
            if Q[x][i]>maximum:
                maximum=Q[x][i]
                pos=i
            i=i+1
        x=pos
    print(" 5")
    print("Complete")
    print("Enter done : Y/N")
    done=input()

print("Training ang exploration done!!")
        
        
        
        

        
        
            
            
       # Q[Current_Sate][action]=R[Current_State][action]+(Gamma*)
                
            



