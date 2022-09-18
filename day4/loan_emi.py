

p = float(input('Principal loan amount'))
n= float(input('Loan tenure in months'))
r = float(input('Annual interest rate'))
r = r/12/100

#If rate of interest is 7.2% p.a. then r = 7.2/12/100 = 0.006
emi = p*r*(((1+r)**n)/ (((1+r)**n)-1) )
print(emi)