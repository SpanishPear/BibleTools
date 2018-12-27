import random as rand
import csv
BibleCsvPath = "bible_data_set.csv"
def GetRandEven():
    number = rand.randint(1,31102)
    if number % 2 == 0:
        new = number
        return new
    else:
        return GetRandEven()

def GetRandomVerse():
    with open(BibleCsvPath) as f:
        wholeFile = list(csv.DictReader(f))
        rowNumber = int(GetRandEven())
        row = wholeFile[rowNumber]
        print()
        print(row["text"])
        return(row["citation"], rowNumber)

def GetVerse(rowNumber):
    with open(BibleCsvPath) as f:
        wholeFile = list(csv.DictReader(f))
        row = wholeFile[rowNumber]
        print()
        print(row["text"])
        return rowNumber

def GuessCitatation(citation):
    guess = input("enter your guess! Please ensure it's in the form Book chapter:verse , eg 1 John 1:1  : ")
    if guess == citation:
        return True
    else:
        return False

def EndGame(actioncount):
    print("Congratulations! You gussed correctly!")
    score = int(10000 - 8*(actioncount))
    print("your final score is:", str(score) +"/10000")

def ShowHelp():
    print("\n\nCommands \nnext -- Shows next verse\nprevious -- Shows previous verse \nguess -- guess the bible verse(format 'book chapter:verse')\n\n")


def Driver():
    #GetRandomVerse("bible_data_set.csv")
    GuessBibleGame()

def GuessBibleGame():
    #printing the commands
    ShowHelp()
    guessed = False
    dataset = GetRandomVerse() #set the dataset to the return of the function call, otherwise if you call it twice it will result in having the citation not match the row number
    target = dataset[0] #target is the citation (eg Geneisis 1:1)
    originalRowNumber = dataset[1] #this will not be mutated
    rowNumber = dataset[1] #this will be mutated
    actions = 0 #action counter for scoring system
    command = input("Enter a command: ")
    print(target)
    #command loop
    while guessed == False:
        #get next verse
        if command.lower() == "next":
            rowNumber = GetVerse(rowNumber + 1)
            actions += 1
            command = input("Enter a command: ")

        elif command.lower() == "previous":
            actions += 1
            rowNumber = GetVerse(rowNumber - 1)
            command = input("Enter a command: ")

        elif command.lower() == "guess":
            if GuessCitatation(target) == True:
                guessed = True
                EndGame(actions)
                break
            else:
                #making an incorrect guess loses more points
                print("Incorrect!!\n")
                actions += 2
                command = input("Enter a command: ")

        else:
            command = input("Please enter a valid command: ")

# __name__ == __main__ ensures that if this file is being imported, the function is still called.
if __name__ == "__main__":
    Driver()
