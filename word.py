class Counter:
	sen="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
	sen=sen.split(" ")
	sen2=[]
	for i in sen:
		if i not in sen2:
			sen2.append(i)
	for i in range(0,len(sen2)):
		print('Frequency of', sen2[i], 'is :', sen.count(sen2[i]))
