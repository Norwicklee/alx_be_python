def safe_divide(numerator, denominator):
  """
  Performs division with error handling for division by zero and non-numeric inputs.

  Args:
    numerator (str or float): The numerator of the division operation.
    denominator (str or float): The denominator of the division operation.

  Returns:
    str: A message indicating the result or error encountered.
  """
  try:
    # Attempt to convert arguments to floats for division
    numerator = float(numerator)
    denominator = float(denominator)
    result = numerator / denominator
    return f"The result of the division is {result:.2f}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
      return "Error: Please enter numeric values only."
