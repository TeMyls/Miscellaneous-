import random
from typing import *

def count_occurences_r(substring: str,string: str, cindex = 0):
	ind = string.find(substring, cindex)
	if not substring:
		return 0
	
	if ind == -1:
		return 0
	
	
	if ind!= -1:
		return count_occurences(substring,string,ind+1) + 1
		
def count_occurences_i(substring: str,string: str):
	occur = 0
	ind = string.find(substring, 0)
	if not substring: 
		return 0
	if ind == -1:
		return 0
	while ind != -1:
		occur += 1
		ind = string.find(substring, ind + 1)
		
	return  occur
	
def count_occurences_lc(sub,stg):
	return len([i for i in range(0,len(stg),len(sub)) if stg[i:i + len(sub)] == sub])
	


	

string = 'sss'
substring = 's' 
print(count_occurences_i(substring, string))
print(count_occurences_i('hh',"hhfhgggvhhdhrhjthhgddhyghdhtgssghrgvghhtjgdhhhffhbvvjh"))
