def add_time(start, duration, day_of_week=None):

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

    # Read inputs
    s_hour = int(start.split(':')[0])
    s_mins = int(start.split(':')[1].split(' ')[0])
    s_midday = start.split(' ')[1]

    d_hours = int(duration.split(':')[0])
    d_mins = int(duration.split(':')[1].split(' ')[0])

    if day_of_week:
        day_of_week = day_of_week.lower().title()
        day_of_week_index = week.index(day_of_week)
    else:
        day_of_week_index = 0

    days_ahead = 0
    new_day_of_week = day_of_week
    if d_hours >= 24:
        days_ahead = int(d_hours / 24)
        d_hours = d_hours % 24
        print(days_ahead)

    new_mins = s_mins + d_mins
    if new_mins >= 60:
        d_hours += 1
    new_mins = new_mins % 60

    new_hours = s_hour + d_hours
    if new_hours >= 12 and s_midday == 'AM':
        new_midday = 'PM'
    elif new_hours >= 12 and s_midday == 'PM':
        days_ahead += 1
        new_midday = 'AM'
    else:
        new_midday = s_midday

    if new_hours > 12:
        new_hours = new_hours % 12

    if new_mins < 10:
        new_mins = f'0{new_mins}'

    new_time_hrs = f'{new_hours}:{new_mins} {new_midday}'
    if day_of_week:
        new_day_of_week_index = (day_of_week_index + days_ahead) % 7
        new_day_of_week = week[new_day_of_week_index]
        if days_ahead > 1:
            new_time = f'{new_time_hrs}, {new_day_of_week} ({days_ahead} days later)'
        elif days_ahead == 1:
            new_time = f'{new_time_hrs}, {new_day_of_week} (next day)'
        else:
            new_time = f'{new_time_hrs}, {new_day_of_week}'
    else:
        if days_ahead > 1:
            new_time = f'{new_time_hrs} ({days_ahead} days later)'
        elif days_ahead == 1:
            new_time = f'{new_time_hrs} (next day)'
        else:
            new_time = f'{new_time_hrs}'

    print(new_time)
    return new_time

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")