# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# Print the expected output - 50
# SampList : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#   Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


elist=[]
SampList=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(0,len(SampList)):
    for j in range(0,len(SampList)-1):
        if(SampList[j][1]>SampList[j+1][1]):
            elist=SampList[j]
            SampList[j]=SampList[j+1]
            SampList[j+1]=elist
   
    print(SampList)
    print(elist)      