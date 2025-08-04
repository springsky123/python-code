#WAP to read studend data from a csv file and display names of students who scored above 90

import csv


#function to print the student name
def studentmark():
    try:
        file = open('record.csv','r')
        read = csv.reader(file)
        next(read)
        for row in read:
            if row==[]:
                pass
            else:
                if int(row[4])>90:
                    print(row[0])
                else:
                    pass
    except:
        print("No contents found in the file...")
print("Names of students whose marks are above 90:")
studentmark()
