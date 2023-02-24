import csv

# path to the file
path_csv_file = 'csv_files/csv_1.csv'
path_text_file = "text_files/text.txt"
path_text_file2 = "text_files/text2.txt"

with open(path_text_file) as text_file:
    pass

with open(path_text_file2, "w") as text_file2:
    pass

with open(path_csv_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    for i in csv_reader:
        print(i)
 


