def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input(" please Enter  your weight in kilograms: "))
height = float(input(" please Enter  your height in meters: "))

bmi = calculate_bmi(weight, height)


print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 20:
    print("You have a normal weight.")
elif bmi < 25:
    print("You are overweight.")
elif bmi < 35:
    print("You have a Obesity.")
else:
    print("value error please try again")
