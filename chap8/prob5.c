try:
    num = float(input("\Enter a number: "))
except:
    print("Something went wrong!")
    
try:
    num = float(input("\Enter a number: "))
except(ValueError):
    print("That was not a number!")
    
for value in (None, "Hi"):
  try:
    print("Attempting to convert", value, "->", end =" ")
    print(float(value))
  except(TypeError, ValueError):
    print("Something went wrong")
print("")

for value in (None, "Hi"):
    try:
      print("Attempting to convert", value, "->", end =" ")
      print(float(value))
    except(TypeError):
      print("I can only convert a string or a number!")
    except(ValueError):
      print("I can only convert a string or a digits!")
print("")  

try:
  num = float(input("Enter a number: "))
except ValueError as e:
  print("Not a number! or as python would say\n", e)
print()

try:
  num = float(input("Enter a number"))
except(ValueError):
  print("Tat was not a number")
else:
  print("you entered the number ", num)
