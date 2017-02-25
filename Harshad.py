Harshad = []
Product= []
for i in range(1,1001) :

 digit = list(str(i))
 Digit_Sum= 0
 Digit_Product= 1
 for j in digit :
  Digit_Product = int(j) * Digit_Product
  Digit_Sum = int(j) + Digit_Sum
 if Digit_Product != 0 :
  if i % Digit_Sum ==0 :
   Harshad.append(i)
  if i % Digit_Product==0:
   Product.append(i)
print "Harshad numbers from 1 to 1000"
print Harshad
print "Numbers that can be divided by the product of their digits"
print Product
