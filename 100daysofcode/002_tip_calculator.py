print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("How many people to split th bill? "))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15? ")
)
total = total_bill + total_bill * tip_percentage / 100
person_total = total / number_of_people
print(f"Each person should pay ${person_total:.2f}")
