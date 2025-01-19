class BankAccount:
  """
  A simple bank account class to demonstrate OOP concepts.
  """

  def __init__(self, initial_balance=0.0):
    """
    Initializes a BankAccount object with an optional starting balance.

    Args:
      initial_balance (float, optional): The initial balance of the account. Defaults to 0.0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits the specified amount into the account balance.

    Args:
      amount (float): The amount to be deposited.

    Raises:
      ValueError: If the deposit amount is negative.
    """
    if amount < 0:
      raise ValueError("Deposit amount cannot be negative.")
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Withdraws the specified amount from the account balance if sufficient funds exist.

    Args:
      amount (float): The amount to be withdrawn.

    Returns:
      bool: True if the withdrawal was successful, False otherwise.
    """
    if amount > self.account_balance:
      return False
    self.account_balance -= amount
    return True

  def display_balance(self):
    """
    Prints the current account balance in a user-friendly format.
    """
    print(f"Your current balance is: ${self.account_balance:.2f}")