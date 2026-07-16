def run(items: dict) -> bool:
    all_same = False
    if len(items) <= 1:
        all_same = True
    else:
        counter = 1
        for value in items.values():
            if counter == 1:
                value_to_comparate = value
                counter += 1
            elif value == value_to_comparate:
                all_same = True
                value_to_comparate = value
                

            else:
                all_same = False
                break
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
