def run(marks: dict) -> tuple:
    passed = {name.upper() : note for name, note in marks.items() if note >= 5}
    failed = {name.lower() : note for name, note in marks.items() if note < 5}


    return passed, failed


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
