import random as rand
import csv

def GetRandEven():
    number = rand.randint(1,31102)
    if number % 2 == 0:
        new = number
        return new
    else:
        return GetRandEven()

def GetRandomVerse(BibleCsvPath):
    with open(BibleCsvPath) as f:
        wholeFile = list(csv.DictReader(f))
        random = int(GetRandEven())
        row = wholeFile[random]
        print(row["text"])

def Driver():
    GetRandomVerse("bible_data_set.csv")


Driver()
