# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

def parseStringAdi (string):
	counter=0
	name=''
	digitInTagString=''
	digitInTagDigit=0
	inTag=''
	tags={}
	counterChar=0
	for i in string:
		counter=counter+1;
		if i=='<':
			counterChar=counter
			while string[counterChar]!=':':
					name=name+string[counterChar]
					counterChar=counterChar+1
			if string[counterChar]==':':
					counterChar=counterChar+1
					while string[counterChar]!='>':
						digitInTagString=digitInTagString+string[counterChar]
						counterChar=counterChar+1
						digitInTagDigit=int(digitInTagString)
			while  string[counterChar]!='<'  :
					if string[counterChar]!=">": 
							inTag=inTag+string[counterChar]
					if counterChar==len(string)-1:
						break
					else:
						counterChar=counterChar+1
					
		
		tags.update({name:inTag})
		name=''
		inTag=''	
	return tags			

## For example using string			
string='<CALL:5>UR4LGA<NAME:6>Sergey<RST:2>599'
## call parse function
tags=parseStringAdi(string) # function return Python-dictionary 
## Example result out in console		
print('Name: ' + tags.get('NAME') + '\nCall: ' + tags.get('CALL') + '\nRS:' + tags.get('RST'))


		


