import numpy
import random
l =0
text=open('text.txt').readlines()
f=open("updated_text.txt","a")	
lis=[]
length=0
for t in text:
	word=t
	s=0
	for w in word:
		s=s*10+ord(w)
		s=s%1000000007
	lis.append(s)
	f.write(str(s))
	length=length+1
	f.write(",")
while(length < 5000):
	f.write("0")
	f.write(",")
	length=length+1
f.write(" 1\n")
l=lis
for i in xrange(1,10):
	number_of_random_frames=random.randint(0, 30)
	lis=l
	for j in xrange(1,number_of_random_frames):
		index1 = random.randint(-1,len(lis)-1)
		index2 = random.randint(-1,len(lis)-1)
		lis[index1],lis[index2]=lis[index2],lis[index1]
		length=0
		for num in lis:
			f.write(str(num))				
			f.write(",")
			length+=1
		while(length < 5000):
			f.write("0")
			f.write(",")
			length=length+1	
		f.write(" 0\n")

for i in xrange(1,10):
	number_of_random_frames=random.randint(0, 30)
	lis=l
	for j in xrange(1,number_of_random_frames):
		index1 = random.randint(-1,len(lis)-1)
		lis.remove(lis[index1])
		length=0
		if cmp(lis,l)!=0:
			for num in lis:
				f.write(str(num))				
				f.write(",")
				length+=1
			while(length < 5000):
				f.write("0")
				f.write(",")
				length=length+1	
			f.write(" 0\n")
f.close()