def math():
	a=input(" ")
	b=input(" ")
	print(f"add=int({a+b})")
	print(f"sub=int({a-b})")
	print(f"mul=int({a*b})")
	if b==0:
		print("zero div error")
	else:
		print(f"div=int({a / b})")
while True:	
	math()
	choice=int(input("enter 0 to exit"))
	if choice==0:
		break