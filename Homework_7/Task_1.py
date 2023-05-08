import csv


usd_exchange = 36.57

with open('test_file.csv', 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)

    new_rows = []

    for row in csv_reader:
        name = row[0]
        salary_uah = [round(float(salary) * usd_exchange) for salary in row[1:]]
        new_row = [name] + salary_uah
        new_rows.append(new_row)


with open('salaries_uah.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    csv_writer.writerows(new_rows)
