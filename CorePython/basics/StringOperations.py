'''
Created on 03-Apr-2018

@author: ajitj
'''
#Split multiline into lines:
mulLines = '''Please correct the following errors :

-The help link for user is not a valid url.
-The share help link for user is not a valid url.'''
newList=[]
lineList = mulLines.splitlines()
print(len(lineList))
for line in lineList:
    newLine = line;
    if not len(line)==0:
        newList.append(newLine)
    print (newLine)

print (len(newList))    
newList = [str(newList[x]) for x in range(len(newList))]
print ("The help link for user is not a valid url." in newList)
print ("Actual lines:%s" %(newList))

#String concatination demo
str1 = "This is test"
if("This is test"==str1):
    print ("true")
print (str1+" by Ajit.")   

