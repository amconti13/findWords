

#-------------------------------------------------------------------------------
def get_datalines (filename = "") : #function with default value
    if not filename : #if they dont give us a file name
        filename = input("Enter file to earch: ")
    fileobj = open(filename, "r")
    data = fileobj.readlines() #read all data lines in one list
    fileobj.close()
    return data

#-------------------------------------------------------------------------------
def cleanwords(dataline) :

    for word in dataline.split() : #word in list of split up strings from dataline
        word = word.strip(",.?!'\"()")
        word = word.upper()
        yield word #gives it back one by one

#-------------------------------------------------------------------------------
def get_worddictionary( lines ) :

    dictionary = {}
    linenum = 1

    for line in lines :
        for word in cleanwords(line) : #adding words into dictionary
            if word in dictionary : #if its in the dictionary already
                dictionary[word].add(linenum) #add line number into the set
            else :
                dictionary[word] = {linenum}

        linenum += 1
    return dictionary
#-------------------------------------------------------------------------------
def replace_word( line, word ) :
    searchline = line.lower()
    searchword = word.lower()
    index = searchline.find(searchword)

    while index != -1 :
        line = line[ 0 : index ] + word.upper() + line[ index + len(word) : ]
        index = searchline.find( searchword, index + len(word) )
    
    return line



#-------------------------------------------------------------------------------
def display_words_in_line( line, linenum, word1, word2 = "" ) :
    
    line = replace_word( line, word1 )
    if word2:
        line = replace_word( line, word2 )
    print( linenum, line, sep = ": " )

#-------------------------------------------------------------------------------




datalines = get_datalines("/Users/Conti/Desktop/KKK.txt")
worddict = get_worddictionary(datalines)



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
            for linenum in sorted(list(lines)) :
                display_words_in_line(datalines[linenum-1], linenum, query)
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
