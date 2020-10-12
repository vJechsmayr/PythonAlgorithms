#try except
data_valid = False
while data_valid == False:
        while True:
            grade1=input("Enter Marks of test 1: ")
            try:
               grade1=int(grade1)
               break
            except:
               print("Invalid Grade")
        if (grade1<0 or grade1>10):
            print("Invalid Grade")
        else:
            data_valid=True
while data_valid == True:
        while True:
              grade2=input("Enter Marks of test 2: ")
              try:
                grade2=int(grade2)
                break
              except:
                print("Invalid Grade")
        if (grade2<0 or grade2>10):
              print("Invalid Grade")
        else:
              data_valid=False

while data_valid == False:
       while True:    
          absences=input("Enter Absences: ")
          try:
            absences=int(absences)
            break
          except:
            print("Invalid Grade")
       if (absences<0):
           print("inavalid absenties")
       else:
           data_valid=True

while data_valid == True:
       while True:        
          total_classes=input("Enter Total classes: ")
          try:
            total_classes=int(total_classes)
            break
          except:
            print("Invalid Grade")
       if (total_classes<=0):
           print("inavalid classes")
       else:
           data_valid=False
      
average=(grade1 + grade2)/2
presences=((total_classes-absences)/total_classes)*100
print("Your avareage grade is ",average,"and total percentage of presentie is ",presences,"%")
if (average>6):
     if(presences>80):
        print("You are passed!!CONGRATULATIONS")
     else:
        print("oops!!You are failed due to less Presenties..TRY AGAIN LATER")
else:
     print("oops!!You are failed due to less grade..TRY AGAIN LATER")

