#2. Write a program to find simple interest on a principal amount A at interest rate of R for time 
# period T. Take A, R and T as input from the user.

A = float(input('Enter Amount'))
R = float(input('Enter the rate of interest'))
T = float(input('Enter the time period'))

interest = A*(R/100)*T
print(interest)
