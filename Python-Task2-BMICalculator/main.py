
# ==============================
# BMI Calculator
# Oasis Infobyte Internship
# ==============================

print("================================")
print("       BMI CALCULATOR")
print("================================")

try:
    # Get user details
    name = input("Enter your name: ")

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than zero.")

    else:
        # Calculate BMI
        bmi = weight / (height * height)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal weight"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obese"

        # Display result
        print("\n========== BMI RESULT ==========")
        print("Name:", name)
        print("Weight:", weight, "kg")
        print("Height:", height, "metres")
        print("Your BMI:", round(bmi, 2))
        print("Category:", category)
        print("================================")

except ValueError:
    print("Error: Please enter valid numeric values.")
