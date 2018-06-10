print("This program checks if a whole number is prime or composite. ")
PrimeCheck_In=raw_input("Enter the number")
PrimeCheck=int(PrimeCheck_In)
#print(PrimeCheck)
IsPrime=True
for i in range(2,PrimeCheck-1):
  if (PrimeCheck%i==0):
    IsPrime=False
    break
  else:
    continue
if(IsPrime==True):
  print("Your number is prime")
else:
  print("Your number is composite")