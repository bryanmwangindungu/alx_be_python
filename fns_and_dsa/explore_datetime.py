from datetime import datetime, timedelta

def main():
    # Get the current date and time
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # Ask the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    main()