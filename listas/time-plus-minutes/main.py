def run(time: str, offset: int) -> str:
    hour, minute = time.split(':')
    offset = offset // 60
    hour = int(hour) + offset
    final_time = f'{hour}:{minute}'
    return final_time


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
