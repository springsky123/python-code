import csv

class InvalidScoreError(Exception):
        pass
def add_student_data():
        try:
                name = input("Enter student name:")
                score = int(input("Enter student score:"))
                if not (0<=score<=100):
                        raise InvalidScoreError("invalid score")
                data = [name,score]
        except ValueError:
                print("Invalid value of score!!! ")
        except InvalidScoreError:
                print("Invalid value of score!!! ")
        try:
                file = open("student.csv","a",newline = "")
                writer = csv.writer(file)
                writer.writerow(data)
                print("Student data added successfully... ")
                file.close()
        except FileNotFoundError:
                print("File not found ,Create a starter file..")
def class_average():
        try:
                file = open("student.csv","r")
                read = csv.reader(file)
                count = 0
                sum_score = 0
                next(read)
                for i in read:
                        if i == []:
                                pass
                        else:
                                sum_score+=int(i[1])
                                count+=1
                average = sum_score/count
                print("Average score :",average)
                file.close()
        except FileNotFoundError:
                print("File not found ,Create a starter file..")
def get_top_students(filename="student.csv", num_top=3):
        students = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    students.append(row)
                except ValueError:
                    print(f"Skipping row due to invalid score: {row}")
                    continue

        # Sort students by score in descending order
        students.sort(key=lambda x: x['Score'], reverse=True)

        # Return the top N students
        return students[:num_top]
#function for options to choose 
def choose_option():
    print('......................................')
    print("------------------WELCOME IN THIS PROGRAM-----------------")
    print("1. Add student data")
    print("2. Calculate average")
    print("3. Print Top 3 students")
    print('.......................................')
    choose = int(input('enter your choice:'))
    return choose
#Function to handle the entireprogram        
def main():
        choice = 'y'
        while choice == 'y':
                opt = choose_option()
                if opt == 1:
                        add_student_data()
                elif opt == 2:
                        class_average()
                elif opt == 3:
                        top_students = get_top_students()
                        print("Top 3 Students:")
                        for student in top_students:
                            print(f"Name: {student['Name']}, Score: {student['Score']}")
                else:
                        print("Invalid choice!!!!!!!!!! please try again..")
                        main()
                print()
                choice = input('>Do you want to continue?(type*y*for yes):')
if __name__ == "__main__":
        main()
print()
print("Thank you for visiting this program...")            
                
                
        
