
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

def check_even_odd(num):
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def grade_student(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# Example usage
num = int(input("Enter a number: "))
check_number(num)
check_even_odd(num)

score = int(input("Enter your score: "))
grade_student(score)

age = int(input("Enter your age: "))
check_voting_eligibility(age)

# Bonus condition: checking leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")


