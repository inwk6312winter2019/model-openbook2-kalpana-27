
fin = open("Street_Centrelines.csv","r")

'''#task1
def myfile(fin):
  list1 = []
  for line in fin:
    line=line.split(",")
    list1.append((line[2],line[4],line[7],line[8]))
  print(list1)

myfile(fin)



#Task2


def histogram(fin):
	d={}
	for line in fin:
		line=line.split(",")
		if line[12] not in d:
			d[line[12]]=1
		else:
			d[line[12]]+=1
	print(d)
histogram(fin)


#task3
def unique(fin):
	d={}
	list1 = []
	for line in fin:
		line=line.split(",")
		if line[11] not in d:
			d[line[11]]=1
		else:
			d[line[11]]+=1

	for key in d.keys():
		list1.append(key)
	print(list1)

unique(fin)'''

#Task4

def myfile(fin):
  list1 = []
  d = {}
  for line in fin:  
    line = line.split(",")
    if line[10] not in d:
      d[line[10]]=(line[2])
    print(d)
   

myfile(fin)
