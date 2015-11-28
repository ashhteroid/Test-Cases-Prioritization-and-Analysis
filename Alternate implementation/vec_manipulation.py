
'''  
=================================================================
	@version  3.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	Vector Manipulation Helper module.
=================================================================
'''


'''
input: bitvector as string
output: sum bitvector
'''


def vsum(vstr):
	tot=0
	vec=list(vstr)
	
	for bit in vec:
			tot=tot+int(bit)
	return tot

'''
input: index and location,pname,option
return: vector in string
'''

def vfetch(index,location,pname,option):
	f=open(location+"bit/"+pname+"/result"+str(option)+".txt")
	s=str(f.readlines()[index]).strip('\n')
	f.close()
	return s


'''
input: Two vector strings 
return: sum of merged string and merged string
'''

def vmerge(v1,v2):
	v1=list(v1)
	v2=list(v2)
	v3=[]
	i=0

	for A in v1:
		v3.append(str(int(A) or int(v2[i])))
		i+=1 
	v3=''.join(v3)
	v3sum=vsum(v3)
	return v3sum,v3
