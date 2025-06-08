from datetime import datetime, timedelta

def displaycurrentdatetime():
    """Returns the current date and time formatted as a string."""
    current = datetime.now()
    return current.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days):
    """Takes an integer number of days and returns the future date as a string."""
    current = datetime.now()
    future = current + timedelta(days=days)
    return future.strftime("%Y-%m-%d")

def main():
    # Display current date and time
    print("Current date and time:",displaycurrentdatetime())
    
    try:
        # Get number of days to add from user
        days = int(input("Enter the number of days to add to the current date: "))
        print("Future date:", calculate_future_date(days))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()