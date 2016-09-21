filename = input("Enter file to search: ")
fileobj = open(filename, "r")

worddict = {}
linenum = 0

for line in fileobj :
    wordlist = line.split()

    for index in range(0, len(wordlist)) :
        wordlist[index] = wordlist[index].strip(",.?!'\"()")
        wordlist[index] = wordlist[index].upper()

    for word in wordlist :
        if word in worddict :
            worddict[word].add(linenum)
        else :
            worddict[word] = {linenum}

    linenum += 1

fileobj.close()

answer = "yes"

while answer == "yes" :
    
    query = input("Enter your seach query: ")
    
    querylist = query.split()
    
    if len(querylist) == 1 :
        lines = worddict.get(query.upper())
        if lines == None :
            print("The word" , query, " does not appear in the file")
        else :
            print("The word", query, "appears on lines: ", sorted(list(lines)))
    elif len(querylist) == 2 :
        lines = worddict.get[querylist[1].upper()]
        
        if lines == None :
            print("The word ", query, "does not appear anywhere")
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
