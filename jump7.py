a=list(range(1,101))
for i in a:
	if i%7!=0:
		if int(i/10)!=7:
			if i%10!=7:
				print(i)
