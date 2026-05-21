def run(text1: str, text2: str) -> str:
    limit = len(text1) + len(text1)
    limit_text = limit
    cartesian = ''
    for letter_text1 in text1:
        cartesian += letter_text1
        for letter_text2 in text2:
            cartesian += letter_text2
            if len(cartesian) < limit_text:
                cartesian += letter_text1
            else:
                limit_text += limit
    return cartesian


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
