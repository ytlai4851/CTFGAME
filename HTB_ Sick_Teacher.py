p = {"D":"x","T":"k","Z":'f',"C":'o',"I":'t',"B":'i',"J":'s',"H":'a',"K":'h',"W":'e','N':'m',"S":"d","M":'n','Y':'r',"R":'w',"O":'u',"E":'b',"A":"p","G":"l","Q":'v',"P":'y',"L":'c',"F":"g"}
with open (r'/root/Desktop/ctf.txt','rb') as f1:
	for i in f1:
		s=''
		for j in i :
			if j in p:
				s+=p[j]
			else:
				s+=j
		print(s)
