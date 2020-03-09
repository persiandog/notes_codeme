# BMI = (masa (kg)) / (wzrost (m))²

print('Name?' '')
name = input()


weight = int(input('Weight (kg)?' ''))
print("Thank you.")

height = float(input('Height (m)? ' ''))
print("Thank you.")

bmi = weight / (height **2)

print(name,', Your BMI is: ', round(bmi, 2))

if bmi < 18:
    print("You are underweight")

elif bmi < 25:
    print("You are normal weight")

elif bmi < 30:
    print ("You are overweight")

else:
    print("You are obese")
