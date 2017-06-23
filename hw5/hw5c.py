

def lastLetterIndex():
     # build nested dictionary to store records
     alpha = "abcdefghijklmnopqrstuvwxyz"
     D = {}
     for letter in alpha:
          D[letter] = list(range(134))
          for year in D[letter]:
               # empty dictionary for names in this year
               D[letter][year] = {} 

     # open records of baby names to fill nested dictionary
     names = open("babyNames.txt", "r")
     
     # Loop through records
     for record in names:
          # get record in an array structure
          newRecord = record.strip("\n")
          items = newRecord.split(",")
          
          # isolate individual date in record
          year = int(items[0]) - 1880
          name = items[1]
          gender = items[2]
          numBabies = items[3]
          lastLetter = name[-1]

          # create or update gender frequency records
          if ( D[lastLetter][year].get(name, False) == False ): # need to create record
               if gender == "M":
                    D[lastLetter][year][name] = [("M", numBabies), ("F", 0)]
               else:
                    D[lastLetter][year][name] = [("M", 0), ("F", numBabies)]
          else: # record already exists
               if gender == "M":
                    D[lastLetter][year][name][0] = ("M", numBabies)
               else:
                    D[lastLetter][year][name][1] = ("F", numBabies)
               
     names.close()
     return D


D = lastLetterIndex()
print(D)
     
