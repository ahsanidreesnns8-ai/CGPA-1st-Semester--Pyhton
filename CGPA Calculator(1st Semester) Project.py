#Ahsan Idrees
#2025-CYS-112
import time
print("Welcome to GPA Calculator...")
print("Let's start...")
start=input("Do you want to start program(Y/N): ").upper()
if start=='Y':
    grades={
     "A+": 4.0, 
     "A": 4.0, 
     "A-": 3.7, 
     "B+": 3.3, 
     "B": 3.0, 
     "B-": 2.7, 
     "C+": 2.3, 
     "C": 2.0, 
     "C-": 1.7, 
     "D+": 1.3, 
     "D": 1.0, 
     "F": 0.0
    }
    for keys,values in grades.items():
        print(f'{keys} : {values}')
        time.sleep(0.2)
    total_credit_hours=16
    subjects=int(input("How many subject are you studied in UNI: ")) #lab will be considered as one subject so total probabaly is 8.
    Credit_hour_3=int(input("Enter number of subjects of 3 credit hours: "))
    Credit_hour_2=int(input("Enter number of subjects of 2 credit hours: "))
    Credit_hour_1=int(input("Enter number of subjects of 1 credit hours: "))
    credit_hour=[]
    while True:
        try:
            for i in range(1,Credit_hour_3+1):
                name_3_credit_hour=input(f"Enter name of subject {i} (3 credit hour): ")
                gpa_subject=input(f"Enter grade of that subject {i}: ")
                credit_hour.append(grades[gpa_subject]*3)
            for j in range(1,Credit_hour_2+1):
                name_2_credit_hour=input(f"Enter name of subject {j} (2 credit hour): ")
                name_2_credit_hour=[]
                gpa_subject=input(f"Enter grade of that subject {j}: ")
                credit_hour.append(grades[gpa_subject]*2)
            for k in range(1,Credit_hour_1+1):
                name_1_credit_hour=input(f"Enter name of subject {k} (1 credit hour): ")
                gpa_subject=input(f"Enter grade of that subject {k}: ")
                credit_hour.append(grades[gpa_subject]*1)
            break
        except ValueError:
            raise 'Invalid name given.'
    sum_points=0
    for l in credit_hour:
        sum_points+=l
    gpa=sum_points/total_credit_hours
    print(f"Your GPA is: {gpa:.2f}.")
    print("Congratulations...")
else:
    print("Oops you don't want to calculate your GPA...")
    