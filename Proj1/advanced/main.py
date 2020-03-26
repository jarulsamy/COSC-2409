# Joshua Arulsamy
# Project 1 - Advanced
# 03/25/2020
# COSC 2049 500

# Totals to keep track of
# Each is list, pos correlated with plan.
num_customers = [0, 0, 0]
total_data = [0, 0, 0]
total_taxes = [0, 0, 0]
total_all_bills = [0, 0, 0]
done = False

rates = [24.99, 39.99, 54.99]

while not done:
    # Set to invalid value to emulate a do-while
    num_phones = -1
    plan = -1
    data = -1

    # Prompt the user for data
    name = input("Enter your name: ")

    # Keep prompting the user if input is invalid
    while num_phones < 1 or num_phones > 4:
        num_phones = int(input("Enter how many phones (1 to 4): "))

    while plan < 1:
        plan = int(input("Select a plan (1, 2, or 3): "))

    while data < 0:
        data = int(input("Enter data usage (int): "))

    # Total cost of plans per customer.
    int_plan_charge = 0
    # Total cost of minutes per customer.
    int_min_charge = 0

    for i in range(num_phones):
        print(f"Phone number {i+1}:")
        user_int_plan = input("Do you have an international calling plan [Y/N]: ")
        user_int_min = int(input("Enter international minutes: "))

        # Convert int_plan str input to bool
        if user_int_plan.lower() == "y":
            user_int_plan = True
            int_plan_charge += 20
            if user_int_min > 100:
                int_min_charge += ((user_int_min - 100) * 0.10)
        else:
            user_int_plan = False
            int_min_charge += user_int_min

    # Select the plan
    # Calculate based on corresponding rates
    if plan == 1:
        data_allotment = 0
        rate_charge = rates[0] * num_phones
        data_charge = data * 15
    elif plan == 2:
        rate_charge = rates[1] * num_phones
        data_allotment = num_phones
        if data > data_allotment:
            data_charge = (data - data_allotment) * 10
        else:
            data_charge = 0
    elif plan == 3:
        rate_charge = rates[2] * num_phones
        data_allotment = 3 * num_phones
        if data > data_allotment:
            data_charge = (data - data_allotment) * 7.5
        else:
            data_charge = 0

    # Calculate the rest of the stats
    sub_total = sum([rate_charge, data_charge, int_plan_charge, int_min_charge])
    tax = sub_total * 0.06
    total = sub_total + tax

    # Update the totals
    num_customers[plan - 1] += 1
    total_data[plan - 1] += data
    total_taxes[plan - 1] += tax
    total_all_bills[plan - 1] += total

    # Display the per customer stats
    print(f"\n\t{name}:")
    print(f"\t${format(rate_charge, '.2f')} (Plan: {plan})", end="")
    print(" - Base Rate Charge")

    print(f"\t${format(data_charge, '.2f')} ({format(data, '.2f')}", end="")
    print(f"GB, ${data_allotment} GB Free) - Data Charge")

    print(f"\t{format(int_plan_charge, '.2f')} ({'Yes' if user_int_plan else 'No'}) - International Plan")
    print(f"\t${format(int_min_charge, '.2f')} ({user_int_min} min.) - International Minutes")

    print(f"\t${format(tax, '.2f')} - 6% Tax")
    print(f"\t${format(total, '.2f')} - Total")

    # Stop/Continue Loop
    loop = input("\nAdd another customer? [Y/N]: ")
    if loop.lower() == "n":
        done = True


# Display the totals by plan
for i in range(3):
    print(f"\nPlan {i+1}")
    print(f"\n\t{num_customers[i]} Customer(s).")
    print(f"\t{format(total_data[i], '.2f')} GB downloaded.")
    print(f"\t${format(total_taxes[i], '.2f')} taxes collected.")
    print(f"\t${format(total_all_bills[i], '.2f')} total of all bills.")
    if num_customers[i] == 0:
        print(f"\tN/A average bill.")
    else:
        print(f"\t${format(total_all_bills[i]/num_customers[i], '.2f')} average bill.")
