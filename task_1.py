time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_string = time_string.replace(' ', ',')
time_list = time_string.split(',')
minutes_list = []
TIME_COEFFICIENT = 60

for element in time_list:
    if 'h' in element:
        minutes_list.append(int(element[:-1]) * TIME_COEFFICIENT)
    elif 'm' in element:
        minutes_list.append(int(element[:-1]))
    elif 's' in element:
        minutes_list.append(int(element[:-1]) // TIME_COEFFICIENT)

result = sum(minutes_list)
print(result)