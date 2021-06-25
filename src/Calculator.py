import Operations


def resolve(expression: str):
    """
    Resolves a S-expression computation
    """

    if expression.isnumeric():
        return int(expression)
    if expression[0] != "(" or expression[-1] != ")":
        raise Exception("Invalid Expression")

    tokens = _parse_tokens(expression)

    value, _ = _resolve_expression(tokens[1:])
    return value


def _parse_tokens(expression: str):
    """
    Parses the tokens that makes the S-Expression.
    Note: The performance of this function is not O(1) (At least O(n²))
    """
    return expression.replace("(", "( ").replace(")", " )").split()


def _resolve_expression(tokens, pos=0):
    """
    Understands the symbols in a S-Expression and process the operation
    """

    operation = []
    operands = []
    pending_operands = False

    while pos < len(tokens):
        tkn = tokens[pos]
        if tkn in Operations.OPERATIONS.keys():
            operation.append(tkn)
            pending_operands = True
        elif tkn == ")":
            operation.append(operands)
            return _resolve_operation(operation), pos
        elif tkn == "(":
            value, pos = _resolve_expression(tokens, pos+1)
            operands.append(value)
        elif pending_operands:
            if tkn.isnumeric():
                operands.append(int(tkn))
        else:
            raise Exception(f"Invalid expression: Invalid token at pos:{pos}")

        pos = pos + 1
    return _resolve_operation(operation), pos


def _resolve_operation(operation):
    """
    Calculates a numeric math operation. This method assumes the operation
    exists in Operations.OPERATIONS and the format of operation is
    [operation [...operands]]
    """
    operator = Operations.OPERATIONS[operation[0]]
    return operator(operation[1])
