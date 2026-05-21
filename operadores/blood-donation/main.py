def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    if age in range(18, 65) and weight > 50 and heartbeat in range(50, 110) and platelets > 150000:
        suitable_for_donation = True
    else:
        suitable_for_donation = False
    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
