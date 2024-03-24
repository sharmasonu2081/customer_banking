# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("Please enter your savings account details.")
savings_balance = float(input("Enter the initial balance of the savings account ($): "))
savings_interest_rate = float(input("Enter the annual interest rate (APR) for the savings account (%): "))
savings_months = int(input("Enter the length of time in months the interest will be calculated for: "))
    # Call the create_savings_account function and pass the variables from the user.

updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"\nInterest Earned on Savings Account: ${savings_interest_earned:.2f}")
print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
print("Enter your CD account details:")
cd_balance = float(input("Initial CD account balance ($): "))
cd_interest_rate = float(input("Annual interest rate (APR) (%): "))
cd_months = int(input("Number of months for interest calculation: "))
    # Call the create_cd_account function and pass the variables from the user.
from cd_account import create_cd_account
updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"\nInterest Earned on CD Account: ${cd_interest_earned:.2f}")
print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")
if __name__ == "__main__":
    # Call the main function.
    main()