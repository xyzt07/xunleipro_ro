import hashlib
import base64
sn='ACPZ0F6211991'
mac='B0:D5:9D:35:F1:6E'
enckey='i8e%Fvj24nz024@d!c'
str=sn+mac+enckey
tmp=hashlib.md5()
tmp.update(str)
t=tmp.digest()
s=base64.b64encode(t)
for i in range(len(s)):
	if(ord(s[i])==43):
		s[i]==chr(45)
		
	if(ord(s[i])==47):
		s[i]=chr(95)
			
	
print s[0:8]
