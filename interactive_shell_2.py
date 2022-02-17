#source: https://www.youtube.com/watch?v=B55roI7rE_Y
#create an infinite loop
#">>>" will be the prompt
#for each iteration, take input from user
while 1:
	x = input(">>> ")
#add a break condition    
	if x == 'exit':
		break
#else
	try:
		y = eval(x)
		if y: print(y)
	except:
		try:
			exec(x)
		except Exception as e:
			print("error:", e)