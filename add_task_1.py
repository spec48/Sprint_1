types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def unique_tickets():
    temp_list = []
    for lst in tickets.values():
        for ticket in reversed(lst):
            if ticket in temp_list:
                lst.remove(ticket)
        temp_list += lst
    return tickets


def result_dict(severity_dict, tickets_dict):
    tickets_by_type = {}
    for severity, ticket in zip(severity_dict.values(), tickets_dict.values()):
        tickets_by_type[severity] = ticket
    return tickets_by_type


unique_dict = unique_tickets()
print(result_dict(types, unique_dict))