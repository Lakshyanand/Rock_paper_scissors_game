import random

dad_list=[0]*10
son_list=[0]*10
dad_game={0:'rock',1:'scissor',2:'paper'}
son_game={0:'paper',1:'rock',2:'scissor'}

dad_num=random.randint(0,9)
son_num=random.randint(0,9)

for i in range(10):
    if(i==dad_num):
        a=random.randint(0,2)
        dad_list.append(a)
    else:    
        dad_list.append(int(input()))
    
for i in range(10):
    if(i==son_num):
        b=random.randint(0,2)
        son_list.append(b)
    else:    
        son_list.append(int(input()))
    
result=[]

for i in range(3):
    if(dad_list[dad_num]==i):
        result.append(dad_game[i])
        break

for i in range(3):
    if(son_list[son_num]==i):
        result.append(son_game[i])
        break
    
    
if(result[0]==result[1]):
    print("its a draw")
elif(result[0]=='rock' and result[1]=='scissor'):
    print('dad wins')
elif(result[0]=='rock' and result[1]=='paper'):
    print('son wins')
elif(result[0]=='scissor' and result[1]=='paper'):
    print('dad wins')
elif(result[0]=='scissor' and result[1]=='rock'):
    print('son wins')
elif(resultt[0]=='paper' and result[1]=='scissor'):
    print('son wins')
elif(result[0]=='paper' and result[1]=='rock'):
    print('dad wins')



        

    