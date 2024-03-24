info = input()
company_data_base = {}

while info != 'End':
    company_name, employee_id = info.split(" -> ")
    if company_name not in company_data_base:
        company_data_base[company_name] = [employee_id]
    else:
        if employee_id not in company_data_base[company_name]:
            company_data_base[company_name].append(employee_id)

    info = input()

for (company, employee_ids) in company_data_base.items():
    print(f"{company}")
    print('--', '\n-- '.join(employee_ids))
