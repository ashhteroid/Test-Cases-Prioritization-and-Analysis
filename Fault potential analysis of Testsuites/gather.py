
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

for prior in tlist:
		subprocess.call("python3 fault_analysis.py "+prior,shell=True)




