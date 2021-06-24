"""
Add the needed functional operations to implement here. These should be pure
functional operations
"""


def multiply(iterable):
    acum = 1
    for value in iterable:
        acum = acum * value
    return acum


"""
Supported math operations
"""
OPERATIONS = {
    'add': sum,  # Here we use standard Python sum
    'multiply': multiply  # Here we have an example of custom operation
}
