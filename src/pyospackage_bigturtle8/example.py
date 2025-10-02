"""
A module that adds and subtracts numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b

def sub_numbers(a: float, b: float) -> float:
    """
    Subtract two numbers and return the result.

    Parameters
    ---
    a: float
        The number to subtract from.
    b: float
        The number that subtracts.

    Returns
    ---
    float
        The difference of the two numbers.

    Examples
    ---
    >>> sub_numbers(3, 1)
    2
    >>> sub_numbers(2, 5)
    -3

    """
    return a - b

def mul_numbers(a: float, b: float) -> float:
    """
    Multiplies two numbers and return the result.

    Parameters
    ---
    a: float
        The first number to multiply.
    b: float
        The second number to multiply.

    Returns
    ---
    float
        The product of the two numbers.

    Examples
    ---
    >>> mul_numbers(3, 6)
    18
    >>> mul_numbers(5, 9)
    45

    """
    return a * b

def div_numbers(a: float, b: float) -> float:
    """
    Divides two numbers and return the result.

    Parameters
    ---
    a: float
        The number to divide from.
    b: float
        The number that divides.

    Returns
    ---
    float
        The quotient of the two numbers.

    Examples
    ---
    >>> div_numbers(12, 3)
    4
    >>> div_numbers(4, 8)
    0.5

    """
    return a / b