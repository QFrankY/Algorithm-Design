
#The Challenge:
#Given a list of words, identify anagrams and output groups of anagrams

#My Approach:
#When you sort the letters in two words that are anagrams of each other,
#you obtain the same string. Since I knew python method to break strings
#down into lists and the method to sort these lists, I decided to take the
#words given in the list and create a second list in which their letters
#are sorted. The index of the sorted word in the new list would match the 
#index of the original word in the given list. Using the second list, I can
#hence identify anagrams and map the results to words in the given list.

#Assume the given list is myList

def findAnagrams(myList):
    myListNew = []
    tempList = []
    tempString =""
    listLen = len(myList)
    
    #Sorting the letters in words and populating the second list
    for x in range (0, listLen):
        tempString = myList[x]
        
        for y in range (0, len(tempString)):
            tempList.append(tempString[y].lower())
     
        tempList.sort()       
        myListNew.append("".join(tempList))
       
        #Reseting variables for next iteration
        tempList = []
        tempString =""
    print (myList)
    print (myListNew)
    
    #Grouping and outputing anagrams
    while (len(myList)>0):
        tempList = [myList[0]]
        exitLoop = False
        index = 1
        
        while (not exitLoop and len(myList) > 1):
            
            #If an anagram is found
            if (myListNew[0] == myListNew[index]):
                tempList.append(myList[index])
                
                #Remove these elements as they are already grouped
                del myList[index]
                del myListNew[index]
            
            #Moving onto the next word in the list
            else:
                index +=1
            
            #Since list length is changing within the iteration of the loop
            #This checks if we have reached the end of the list
            if (index >= len(myList)):
                exitLoop = True
        
        #After anagrams are populated into the temporary list, they are removed
        #from consideration
        del myList[0]
        del myListNew[0]
        print(tempList)
    print("done")

#Testing    
myList = ["race","car","reac","rac","arc","time", "eitm", "hello"]
findAnagrams (myList)

#Output:
#['race', 'car', 'reac', 'rac', 'arc', 'time', 'eitm', 'hello']
#['acer', 'acr', 'acer', 'acr', 'acr', 'eimt', 'eimt', 'ehllo']
#['race', 'reac']
#['car', 'rac', 'arc']
#['time', 'eitm']
#['hello']
#done
