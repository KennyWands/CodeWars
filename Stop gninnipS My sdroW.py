def spin_words(sentence):
    newSentence= ""
    newList =[]
    finished=" "
    flag=0
    
    if len(sentence)<= 4:
      
        finished = sentence
        
    elif len(sentence)>= 5:# check long enough sentence
        words =sentence.split (" ")# split on whitespace
        print(words)##
        
        for word in words:## for each element
            if len(word)<=4 and flag > 0 :# add short to list                                   unchanged with space
                newList.append(" "+ word)
                print(word)
            elif len(word)<=4 and flag ==0:
                newList.append(word)
                print(word)
            elif len(word)>=5 and flag != 0:# add long to list in                               reverse
                reverse =word[::-1]
                newList.append(" " + reverse)
                print(word)
            elif len(word)>=5 and flag == 0:
                reverse =word[::-1]
                newList.append(reverse)
                print(word)
            flag = flag+1 
            finished = newSentence.join(newList)
    
    return finished
