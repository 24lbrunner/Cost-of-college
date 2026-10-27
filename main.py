"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    course_cost = credit_cost * CS1430_CREDITS
    return course_cost / CS1430_MEETINGS_PER_SEMESTER


def cost_of_skipped_classes(annual_cost, credits, skipped_count):
    """Calculate the total cost of missed CS 1430 classes."""
    return cost_per_class(annual_cost, credits) * skipped_count
# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Total cost for one year in dollars: "))
    credits = int(input("Credits this semester: "))

    while True:
        # Show your menu here.
        print("\nTHE COST OF COLLEGE")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class")
        print("6. Cost of skipped CS 1430 classes (Worth It?)")
        print("Q. Quit")


        choice = input("Choose an option: ").strip().upper()

        if choice == "1":
            res = cost_per_semester(annual_cost)
            print(f"One semester costs ${res:,.2f}")
        elif choice == "2":
            res = cost_per_month(annual_cost)
            print(f"One month costs ${res:,.2f}")
        elif choice == "3":
            res = cost_per_day(annual_cost)
            print(f"One class day costs ${res:,.2f}")
        elif choice == "4":
            res = cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${res:,.2f}")
        elif choice == "5":
            res = cost_per_class(annual_cost, credits)
            print(f"Every CS 1430 class costs ${res:,.2f}")
        elif choice == "6":
            skipped = int(input("How many CS 1430 classes did you skip?"))
            total_missed = cost_of_skipped_classes(annual_cost, credits, skipped)
            print(f"Skipping {skipped} classes cost you ${total_missed:,.2f}")
        elif choice == "Q":
            print("Thanks for running the numbers!")
            break
        else:
            print("Invalid selection. Please choose a valid option (1-6 or Q).")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
