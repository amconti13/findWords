filename = input("Enter file to search: ")
fileobj = open(filename, "r")

worddict = {}
linenum = 1 #normal people start counting with 1

for line in fileobj :
    wordlist = line.split()

    for index in range(0, len(wordlist)) : #for the length of the wordlist
        wordlist[index] = wordlist[index].strip(",.?!'\"()")
        wordlist[index] = wordlist[index].upper() #can do either lower or upper
    #by now list of words are stripped of punctuation and all uppper case
    for word in wordlist : #adding words into dictionary
        
        if word in worddict : #if its in the dictionary already
            worddict[word].add(linenum) #add line number into the set
        else : #if its not in the dictionary, add it into the dictionary
            worddict[word] = {linenum}

    linenum += 1

fileobj.close() #done processing the file.

answer = "yes"

while answer == "yes" :
    
    query = input("Enter your seach query: ")
    
    querylist = query.split() #to be able to look how many items
                              #are in the query list
        if len(querylist) == 1 : #one item in the query list
            lines = worddict.get(query.upper())#set of line numbers for the word
                            # return None or set that is there
        if lines == None : #without this the program will blow up
            print("The word" , query, " does not appear in the file")
        else :
            print("The word", query, "appears on lines: ", sorted(list(lines)))
#NOT
    elif len(querylist) == 2 :
        lines = worddict.get[querylist[1].upper()]
        
        if lines == None :
            print("The word ", query, "does not appear anywhere.")
        else :
            alllines = set()

            for num in range(1, linenum) :
                alllines.add(num)
            result = alllines - lines
            print("The word ", querylist[1], "does not appear on lines: ",
                  sorted(list(result)))

    else :
#AND
        if querylist[1] == "AND" :
            lines1 = worddict.get(querylist[0].upper())
            lines2 = worddict.get(querylist[2].upper())

            if lines1 != None and lines2 != None :
                result = lines1 & lines2
                print("The words", querylist[0], "and", querylist[2],
                          "exist on lines: ", sorted(list(result)))
            else :
                print("The words to dnot occur on the same line anywhere")
#OR
        elif querylist[1] == "OR" :
            lines1 = worddict.get(querylist[0].upper())
            lines2 = worddict.get(querylist[2].upper())

            if lines1 and lines2 :
                result = lines1 | lines2
                print("At least one of the words", querylist[0], "or",
                      querylist[2], " exist on lines: ", sorted(list(result)))
            
            elif lines1 and not lines2 :
                result = lines1
                print("The word", querylist[0], " exist on lines: ",
                      sorted(list(result)))

            elif not lines1 and lines2 :
                result = lines2
                print("The word", querylist[2], " exist on lines: ",
                      sorted(list(result)))
#XOR
        elif querylist[1] == "XOR" :
            lines1 = worddict.get(querylist[0].upper())
            lines2 = worddict.get(querylist[2].upper())

            if lines1 and lines2 :
                result = lines1 ^ lines2
                print("At least one of the words", querylist[0], "or",
                      querylist[2], " exist on lines: ", sorted(list(result)))

            elif lines1 and not lines2 :
                result = lines1
                print("The word", querylist[0], " exist on lines: ",
                      sorted(list(result)))
            
            elif not lines1 and lines2 :
                result = lines2
                print("The word", querylist[2], " exist on lines: ",
                      sorted(list(result)))





    answer = input("Do you want to enter another query? ")
