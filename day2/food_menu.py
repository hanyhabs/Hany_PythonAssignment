#Design a food menu app where a user can select an item out of multiple choices shown to the user.
#The item selected by the user is shown to the user as the output.

dish = input('Select a dish: A,B,C,D')
if(dish == 'A'):
    print('Your ordered A')
elif(dish == 'B'):
    print('Your ordered B')
elif(dish == 'C'):
    print('Your ordered C')
elif(dish == 'D'):
    print('Your ordered D')    
else:
    print('404: Food not found')