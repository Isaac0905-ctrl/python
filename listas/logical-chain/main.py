def run(values: list, oper: str) -> bool:
    if len(values) > 1:
        value_to_comparate = values[0]
        for value in values[1:]:
            if oper == 'and':
                result = value_to_comparate and value
                value_to_comparate = result
            else:
                result = value_to_comparate or value
                value_to_comparate = result
    else:
        result = values[0]
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
