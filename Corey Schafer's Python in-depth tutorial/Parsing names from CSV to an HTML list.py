import csv

html_output = ''
names = []

with open ("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/Patrons.csv", 'r') as fi:
    csv_data = csv.reader(fi)
    #print(list(csv_data))

    next(csv_data)
    next(csv_data)

    for line in fi:
        # print([line])
        if line[0] == 'No Reward':
            break

        names.append(f"{line[0]} {line[1]}")

# for name in names:
#     print(name)

html_output += f"<p>There are currently {len(names)} contributors.</p>"

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)


# using DictReader
 

html_output = ''
names = []

with open ("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/Patrons.csv", 'r') as fi:
    csv_data = csv.DictReader(fi)
    #print(list(csv_data))

    # for item in csv_data:
    #     print(item)
    next(csv_data)

    for line in fi:
        # print([line])
        if line['FirstName'] == 'No Reward':
            break

        names.append(f"{line['FirstName']} {line['LastName']}")
        

# for name in names:
#     print(name)

html_output += f"<p>There are currently {len(names)} contributors.</p>"

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
