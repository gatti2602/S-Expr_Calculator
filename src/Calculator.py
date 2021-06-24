from Operations import multiply


class Calculator:
    def __init__(self):
        pass

    '''
    Supported math operations
    '''
    _OPERATIONS = {
        'add': sum, # Here we use standard Python sum
        'multiply': multiply # Here we have an example of custom operation
    }

    @staticmethod
    def resolve(expression: str):
        if expression.isnumeric():
            return int(expression)
        if (expression[0] != "(" or expression[-1] != ")"):
            raise Exception("Invalid Expression")

        tokens = expression.replace("(", "( ").replace(")", " )").split()
        return Calculator._resolve_expression(tokens[1:])

    @staticmethod
    def _resolve_expression(tokens):
        operation = []
        operands = []
        pending_operands = False
        for pos, tkn in enumerate(tokens):
            if tkn in Calculator._OPERATIONS.keys():
                operation.append(tkn)
                pending_operands = True
            elif tkn == ")":
                operation.append(operands)
                operands = []
                pending_operands = False
            elif pending_operands:
                if tkn.isnumeric():
                    operands.append(int(tkn))
            else:
                raise Exception(f"Invalid expression: {tokens}")

        return Calculator._resolve_operation(operation)

    @staticmethod
    def _resolve_operation(operation):
        """
        Calculates a numeric math operation. This method assumes the operation
        exists in _OPERATIONS and the format of operation is
        [operation [...operands]]
        """
        operator = Calculator._OPERATIONS[operation[0]]
        return operator(operation[1])
