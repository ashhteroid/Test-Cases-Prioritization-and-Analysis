
'''  
=================================================================
	@version  3.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Vector Reading Helper module.
=================================================================
'''



'''
Bit vector data
input: 		location,pname,option
returns:	readerlist<index,coverage number,testcase>
'''


import vec_manipulation


def reader(location,pname,option):
	uni=open(location+"universe.txt")
	f=open(location+"bit/"+pname+"/result"+str(option)+".txt")
	vecs=f.readlines()
	i=0
	readerlist=[]
	for line in uni:
		cov=vec_manipulation.vsum(str(vecs[i]).strip('\n'))
		test=str(line).strip('\n')
		tup=(i,cov,test)
		readerlist.append(tup)
		i+=1
	uni.close()
	f.close()
	return readerlist
