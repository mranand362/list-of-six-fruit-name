marks1 = int(input("enter marks1:"))
marks2 = int(input("enter marks2:"))
marks3 = int(input("enter marks3:"))
marks4 = int(input("enter marks4:"))
marks5 = int(input("enter marks5:"))
marks6 = int(input("enter marks6:"))
marks7 = int(input("enter marks7:"))

# check for total percentage
total_percentage = (100)*(marks1 + marks2 + marks3 + marks4 + marks5 + marks6 +marks7) / 700
if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33 and marks4>33 and marks5>33 and marks6>33 and marks7>33) :
    print("you are pass", total_percentage)

else:
    print("you are fail", total_percentage)