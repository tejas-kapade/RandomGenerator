import random as ran
print("Random Values Generator ! , 1.type limit , 2.type range from to, 3.getValues\n")
while(True):
	try:
		lim= int(input("\nType How Much Random values you want ?___"))
		min = int(input("Values from___"))
		max= int(input("To________"))
		print("\nHere are Your Random Values___")
		for a in range(1,lim+1):
			print(a,"___",ran.randint(min,max))
	except:
		print("\ninvalid input, Try again ___\n")
		continue
