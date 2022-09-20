#n number of operations in a list
if __name__ == '__main__':
    N = int(input())
li=[]    
i=0
while(i<N):
    operation = input( )
    task = list(operation.split())
    if('append' in operation):
        li.append(int(task[1]))
    elif('insert' in operation):
        li.insert(int(task[1]),int(task[2]))
    elif('remove' in operation):
        li.remove(int(task[1]))
    elif('sort' in operation):
        li.sort()
    elif('pop' in operation):
        li.pop(-1)
    elif('reverse' in operation):
        li.sort(reverse = True)
    elif('print' in operation):
        print(li)
    else:
        print()
    i+=1
       