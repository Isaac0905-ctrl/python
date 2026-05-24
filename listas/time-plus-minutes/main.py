def run(time: str, offset: int) -> str:
    hour, minutes = time.split(':')
    total_minutes = (int(hour) * 60 + int(minutes)) + offset
    total_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    if total_hours > 23:
        total_hours = total_hours % 24
    final_time = f'{total_hours}:{remaining_minutes:02d}'
    return final_time


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
