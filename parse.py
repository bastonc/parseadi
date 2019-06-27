# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

def parseStringAdi (string):
	"""
	This function recieving string from adi-file, and parse it. Function returning result in Phyton dictionary type, where key - it key from ADI-tag, 		value - information from ADI
	"""
#print(len(string.decode('utf-8')))
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
					if name=='EOR':
						break
					counterChar=counterChar+1
			if string[counterChar]==':':
					counterChar=counterChar+1
					while string[counterChar]!='>':
						digitInTagString=digitInTagString+string[counterChar]
						counterChar=counterChar+1
						#digitInTagDigit=int(digitInTagString)
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
string='<BAND:3>20M <CALL:6>DL1BCL <CONT:2>EU <CQZ:2>14 <DXCC:3>230 <FREQ:9>14.000000 <ITUZ:2>28 <MODE:3>SSB <OPERATOR:6>UR4LGA <PFX:3>DL1 <QSLMSG:19>TNX For QSO TU 73!. <QSO_DATE:8:D>20131011 <TIME_ON:6>184700 <RST_RCVD:2>57 <RST_SENT:2>57 <TIME_OFF:6>184700 <eQSL_QSL_RCVD:1>Y <APP_LOGGER32_QSO_NUMBER:1>1<EOR>'
## call prase function
tags=parseStringAdi(string) # function return Python-dictionary type data
## Example result out in console		
print('Band: '+tags.get('BAND')+ '\nCall: '+ tags.get('CALL')+'\nRS:' + tags.get('RST_RCVD') + '\nMODE:' + tags.get('MODE'))


		

