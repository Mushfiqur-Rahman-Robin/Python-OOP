import csv

# with open ("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/Bangladesh all lat and long.csv", 'r') as f:
#     csv_reader = csv.reader(f)

with open("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/Bangladesh all lat and long.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open ("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/new.csv", 'w') as new_file:
        fieldnames = ['districtLabel', 'upazilaLabel', 'lat', 'long']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['lat']
            csv_writer.writerow(line)

    for line in csv_reader:
        print(line['districtLabel'])


    # with open("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/new.csv", 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter = '\t')

    #     for line in f:
    #         csv_writer.writerow(line)
    