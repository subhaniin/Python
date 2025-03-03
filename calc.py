def math():
	a=int(input(" ",))
	b=int(input(" ",))
	print("",f"add={a+b}")
	print("",f"sub={a-b}")
	print("",f"mul={a*b}")
	if b==0:
		print(" zero div error")
	else:
		print("",f"div={int(a/b)}")
while True:	
	math()
	choice=int(input(" enter 0 to exit"))
	if choice==0:
		break