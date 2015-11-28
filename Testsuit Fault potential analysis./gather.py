
'''  
=================================================================
	@version  3.0
	@author   Ashwin Ramadevanahalli
	@title    Testing.


	fault_analysis Helper module.
=================================================================
'''


import subprocess



tlist=["sran","bran","sbran",'stot','btot','sbtot','sadd','badd','sbadd']
plist=['tcas','totinfo','printtokens','printtokens2','replace','schedule','schedule2']
'''
for lol in plist:
	for prior in tlist:
		print prior
		subprocess.call("cd "+lol,shell=True)
		subprocess.call("python3 fault_analysis.py "+prior,shell=True)
		subprocess.call("cd ..",shell=True)
'''
print "Wrirting results "
subprocess.call("rm Finalresults",shell=True)
res=open("Finalresults","w")
count=0
tot=0
for lol in plist:
	res.write(lol+" analysis.\n")
	for prior in tlist:
		count=0
		tot=0
		f=open(lol+"/FResults_"+lol+"_"+prior)
		for line in f:
			tot+=1
			if(line.split()[0]=='1'):
				print line.split()[0]
				count+=1
		f.close()
		res.write("Faults revealed by "+prior+" : "+str(count)+"\n")
	res.write("Total Faults: "+str(tot-2)+"\n")



res.close()
