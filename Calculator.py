def step_by_step_calculator():
    try:
        numbers = int(input("How many numbers do you give? "))
        if numbers < 2:
            print("At least two numbers must be entered.")
            return

        operator = input("Operation (+, -, *, /, average): ").strip()
        result = 0.0

        for i in range(numbers):
            num = float(input(f"{i + 1}. Number: "))
            if i == 0:
                result = num
            else:
                if operator == "+":
                    result += num
                elif operator == "-":
                    result -= num
                elif operator == "*":
                    result *= num
                elif operator == "/":
                    if num == 0:
                        print("You can't divide by zero!")
                        return
                    result /= num
                elif operator == "average":
                    result += num
                else:
                    print("Unknown operation.")
                    return

        if operator == "average":
            result /= numbers

        print("Result:", round(result, 4))

    except ValueError:
        print("Invalid input. A number must be entered.")
    except Exception as e:
        print("An error occurred:", str(e))


def expression_calculator():
    try:
        expression = input("Enter a math expression (e.g. (5 + 2) * 3 - 4 / 2): ")
        result = eval(expression)
        print("Result:", round(result, 4))

    except ZeroDivisionError:
        print("Error: You can't divide by zero.")
    except Exception as e:
        print("Invalid expression:", str(e))


# Main loop
current_mode = None

while True:
    if current_mode not in ["1", "2"]:
        print("\nSelect mode:")
        print("1. Step-by-step calculator")
        print("2. Full expression with parentheses")
        current_mode = input("Enter 1 or 2: ").strip()

    if current_mode == "1":
        step_by_step_calculator()
    elif current_mode == "2":
        expression_calculator()
    else:
        print("Invalid mode selected.")
        current_mode = None
        continue

    print("\nWhat do you want to do next?")
    print("1. Repeat same mode")
    print("2. Switch mode")
    print("3. Exit")
    next_action = input("Enter 1, 2, or 3: ").strip()

    if next_action == "1":
        continue  # repeat same mode
    elif next_action == "2":
        current_mode = None  # re-select mode
    elif next_action == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid selection, exiting.")
        break

input("\nPress Enter to exit...")