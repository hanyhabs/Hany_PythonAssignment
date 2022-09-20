from genericpath import samestat

Result =[]
scorelist = []
if __name__ == '__main__':
    records=[]
    score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    sorted_list=sorted(list(set(scorelist)))[1] 
    for k,v in sorted(Result):
        if v==sorted_list:
            print(k)
        