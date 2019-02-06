fin = open("Street_Centrelines.csv","r")

def myfile(fin):
  list1 = []
  for line in fin:
    line=line.split(",")
    list1.append((line[2],line[4],line[7],line[8]))
  print(list1)

myfile(fin)
