'''
Exercise

Write a program which repeatedly reads numbers until 
the user enters "done". once that is enterd, 
print out the total, count, and average of the numbers. 
if the user enters anything other than a number, detect 
their mistake using try and except and print 
an error message and skip to the next number. 
'''

num = 0
tot = 0
while True:
  val2 = input("Enter a number: ")
  if val2 == "6":
    break
  try:
    flt = float(val2)
  except:
    print("Invalid Input")
    continue
  num += 1
  tot += flt
print("all done")
print(tot, num, tot/num)
