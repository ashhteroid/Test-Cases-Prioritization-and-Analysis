'''  =================================================================
  @version  1.1
  @author   Ashwin Ramadevanahalli
  @title    Testing.
 	 =================================================================

Main module.
######################################################################
'''
import os
import sys
import subprocess
import testset_parse

subprocess.call("rm -r outputs",shell=True)
subprocess.call("mkdir outputs",shell=True)


testset=testset_parse.parse()
print len(testset)