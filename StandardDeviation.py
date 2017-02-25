from math import sqrt
flag = False
while flag == False :
 print "Please give 5 or more numbers seperated with commas (,)"
 User = raw_input()
 try:
    User_List = map(float, User.split(','))
    if len(User_List)>4 :
     flag = True
    else:
        print "Wrong Input"
 except:
      print "Wrong Input"
Num_List =map(float, User.split(','))
print Num_List
Item_Num = len(Num_List)
Num_List.sort()
Sum1 = 0
for i in range(2,Item_Num-2):
 Sum1 =Num_List[i] + Sum1
Mo = Sum1/(Item_Num - 4)
S=0
for i in range (2,Item_Num-2):
 S = pow((Num_List[i] - Mo), 2 ) /(Item_Num-4) + S
Sd = sqrt(S)
print "The standard deviation of the numbers you gave as input is: ", Sd
