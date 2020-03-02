# BMI = (masa (kg)) / (wzrost (m))²
print("Your BMI is: ", 61 / (1.7 **2))


print('Name?' '')
name = input()


weight = int(input('Weight (kg)?' ''))
print("Thank you.")

height = float(input('Height (m)? ' ''))
print("Thank you.")

bmi = weight / (height **2)

print(name,', Your BMI is: ', round(bmi, 2))