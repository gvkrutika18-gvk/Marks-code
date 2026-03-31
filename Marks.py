stud_name=input("ENTER YOUR NAME : ")
roll_no=(int(input("ENTER YOUR ROLL NUMBER : ")
mark_1=(int(input("ENTER YOUR MARK 1 : ")
mark_2=(int(input("ENTER YOUR MARK 2 : ")
mark_3=(int(input("ENTER YOUR MARK 3 : ")
mark_4=(int(input("ENTER YOUR MARK 4 : ")
mark_5=(int(input("ENTER YOUR MARK 5  : ")
grade=(mark_1+mark_2+mark_3+mark_4+mark_5)/5
if(grade>90):
print(stud_name, "has secured GRADE A")
elif(grade>70 and grade<=90):
print(stud_name, "has secured GRADE B")
elif(grade>60 and grade<=70):
print(stud_name, "has secured GRADE C")
elif(grade>50 and grade<=60):
print(stud_name, "has secured GRADE D")
else:
print(NO GRADE")
