##create files output for namespaces
##output1 for percent encoding 
##output2 for extensions

##Clearing out the spaces 
f=open('pagecounts-20160501-000000')
e=open('output10.txt','w')
k=f.readline()
while(k):
	l=k.split()
	if(len(l)==4):
		e.write(k)
	k=f.readline()
f.close()
e.close()

print "Output1"
##Code to capture en and mobile en data
f=open('output10.txt')
e=open('output20.txt','w')
k=f.readline()
while(k):
	l=k.split()
	if(l[0]=="en" or l[0]=="en.m"):
		e.write(k)
	k=f.readline()
f.close()
e.close()

print "Output2"
import os
os.system("python help.py")
f=open('output.txt')	# Code to read the JSON object
n=f.readline()
list1=[]
count=0
while(n):
	n=n[0:-1]
	list1.append(n)
	n=f.readline()
	count=count+1
f.close()

print list1
##Code to filter through namespaces
f=open('output20.txt')
e=open('output30.txt','w')
k=f.readline()
while(k):
	l=k.split()
	flag=0
	for b in list1:
		if b.upper() in l[1].upper():
			ty=len(b)+(l[1].upper()).find(b.upper())
			if(ty==len(b)):
				flag=1
				break
	if(flag==0):
		e.write(k)
	k=f.readline()
f.close()
e.close()

print "Output3"
import os 
os.system("python help1.py")
f=open('output1.txt')	# Code to read percent encoding
n=f.readline()
list1=[]
count=0
while(n):
	n=n[0:-1]
	list1.append(n)
	n=f.readline()
	count=count+1
f.close()

print list1
##Code to filter through percent encoding
f=open('output30.txt')
e=open('output40.txt','w')
k=f.readline()
while(k):
	l=k.split()
	flag=0
	for b in list1:
		if b.upper() in l[1].upper():
			ty=len(b)+(l[1].upper()).find(b.upper())
			if(ty==len(b)):
				flag=1
				break
	if(flag==0):
		e.write(k)
	k=f.readline()
f.close()
e.close()

print "Output4"
##Code to title limitation
f=open('output40.txt')
e=open('output50.txt','w')
k=f.readline()
while(k):
	l=k.split()
	if(l[1][0].isupper() or not l[1][0].isalpha()):
		e.write(k)
	k=f.readline()
f.close()
e.close()

print "Output5"
list1=[".png",".gif",".jpg",".jpeg",".tiff",".tif",".xcf",".mid",".ogg",".ogv",".svg",".djvu",".oga",".flac",".opus",".wav",".webm",".ico",".txt"]
##Code to remove files with the given extension
f=open('output50.txt')
e=open('output60.txt','w')
k=f.readline()
while(k):
	l=k.split()
	flag=0
	for b in list1:
		if b.upper() in l[1].upper():
			ty=len(b)+(l[1].upper()).find(b.upper())
			if(ty==len(b)):
				flag=1
				break
	if(flag==0):
		e.write(k)
	k=f.readline()
f.close()
e.close()

print "Output6"
##Code to remove bolier plate pages 
list1=["404_error/","Main_Page","Hypertext_Transfer_Protocol","Search"]

f=open('output60.txt')
e=open('output70.txt','w')
g=open('output80.txt','w')
k=f.readline()
while(k):
	l=k.split()
	flag=0
	for b in list1:
		if b==l[1]:
			flag=1
			break
	if(flag==0):
		g.write(str(l[1])+" "+str(l[2])+"\n")
		e.write(k)
	k=f.readline()
f.close()
e.close()
g.close()

print "Output7"
##Sorting the file only with titles and page views as this would bring the 
##en and en.m files next to each other
import os
os.system('sort output80.txt > output90.txt')

print "Output8"
##Checking the next file in the page to see if it is a mobile page and 
##adding up page views

f=open('output90.txt')
e=open('output100.txt','w')
k1=f.readline()
k2=f.readline()
l1=k1.split()
if(k2):
	l2=k2.split()
	k=k2
	while(k):
		flag=0
		if(l1[0]==l2[0]):
				l1[1]=str(int(l1[1])+int(l2[1]))
				l2=l1
				k2=k1
				flag=1
		if(flag==0):
			e.write(str(l1[0])+"\t"+str(l1[1])+"\n")
		k=f.readline()
		k1=k2
		k2=k
		l1=l2
		l2=k2.split()
	e.write(str(l1[0]+"\t"+str(l1[1]+"\n")))
else:
	e.write(l1[0]+"\t"+l1[1])
f.close()
e.close()

print "Output9"
##Final sorting
os.system("sort -rk2,2 -k1,1 -t $" " output100.txt > output")
print "Output10"
