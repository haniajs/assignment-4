days_in_year = 365
hours_in_day = 24
minutes_per_hour = 60
second_per_minutes = 60

def main():
    total_second = days_in_year * hours_in_day * minutes_per_hour * second_per_minutes

    print(f"There are {total_second} seconds in a year.")

if __name__ == '__main__':
    main()