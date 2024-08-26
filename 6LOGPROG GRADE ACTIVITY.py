# PINEDA, SOPHIA KEZIAH G.  ICT - 107

prelim_grade = 0.0
midterm_grade = 0.0
finalterm_grade = 0.0

subject = input("Subject: ")

if subject in ['6LOGPROG', '7FunCom']:
    prelim_grade = float(input("Prelim Grade: "))
    midterm_grade = float(input("Midterm Grade: "))
    finalterm_grade = float(input("Finalterm Grade: "))

    
    compute = (prelim_grade + midterm_grade + finalterm_grade) / 3

    if compute >= 97.0:
        classification = "Outstanding"
        equivalent = 1.00
    elif compute >= 94.0:
        classification = "Excellent"
        equivalent = 1.25
    elif compute >= 91.0:
        classification = "Superior"
        equivalent = 1.50
    elif compute >= 88.0:
        classification = "Very Good"
        equivalent = 1.75
    elif compute >= 85.0:
        classification = "Good"
        equivalent = 2.00
    elif compute >= 82.0:
        classification = "Satisfactory"
        equivalent = 2.25
    elif compute >= 79.0:
        classification = "Fairly Satisfactory"
        equivalent = 2.50
    elif compute >= 76.0:
        classification = "Fair"
        equivalent = 2.75
    elif compute >= 75.0:
        classification = "Passed"
        equivalent = 3.00
    else:
        classification = "Failed"
        equivalent = "N/A"


    if subject == '6LOGPROG':
        print(f"Your Grade in {subject} is {compute:.2f} with an Equivalent of {equivalent} and a general classification of VERY GOOD.")
    elif subject == '7FunCom':
        print(f"Your Grade in {subject} is {compute:.2f} with an Equivalent of {equivalent} and a general classification of SUPERIOR.")
else:
    print("Invalid subject.")
