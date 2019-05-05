print("**********************Marksheet**************************")
biology=int(input("Enter the number of Biology subject :"))
chemestry=int(input("Enter the number of Chemestry subject :"))
english=int(input("Enter the number of  English subject :"))
pak_std=int(input("Enter the number of Pakistan Studies subject :"))
sindhi=int(input("Enter the number of Sindhi subject :"))
total_number=int(input("Enter the total number :"))
percentage=biology+english+chemestry+pak_std+sindhi/total_number*100
if(percentage>=80):
    print("Grade : A1")
elif(percentage>=70):
    print("Grade : A")
elif (percentage >= 60):
    print("Grade : B")
elif (percentage >= 50):
    print("Grade : C")
elif (percentage >= 40):
    print("Grade : D")
else:
    print("FAIL")
