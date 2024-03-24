"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):   
    # Create an instance of the Account class with the initial balance and an initial interest of 0.

    savings_account = Account(balance, 0)  # Interest is initially set to 0, as it will be calculated next.
    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate/100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_earned)
    # Return the updated balance and interest earned
      # ADD YOUR CODE HERE
    return updated_balance, interest_earned 