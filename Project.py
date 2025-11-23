def calculate_monthly_saving():
    print("=== Monthly Savings & Goal Planner ===")

    # Gather basic monthly cost info from the user
    income = float(input("What's your monthly income? "))
    rent = float(input("Your Monthly rent (0 if none): "))
    food = float(input("your monthly food cost: "))
    transport = float(input("your Transport expenses: "))
    other_expenses = float(input("Any other  expenses: "))

    # Savings goal the user wants to reach
    goal_amount = float(input("\nHow much money are you trying to save? "))

    # Add up normal expenses to figure out what's left each month
    total_spent = rent + food + transport + other_expenses
    monthly_leftover = income - total_spent

    print(f"\nTotal monthly expenses: {total_spent:.2f}")
    print(f"Money left after expenses: {monthly_leftover:.2f}")

    # If nothing is being saved, inform the user
    if monthly_leftover <= 0:
        print("\nYou're not saving anything right now.")
        print("Try to do less expenses or increasing income to reach your goal.")
        return

    # Estimate time needed to reach the goal
    months = goal_amount / monthly_leftover
    years = int(months // 12)
    leftover_months = int(months % 12)

    print(f"\nTo save {goal_amount:.2f}, it will take roughly {months:.1f} months.")
    print(f"That's about {years} years and {leftover_months} months.")

if __name__ == "__main__":
    calculate_monthly_saving()
