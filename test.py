import csv

def demo_csv():
    #problem with this is that the header ends up sorted as well
    with open('test_file.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        sorted_reader = sorted(csv_reader, key=lambda x: x[2])
        with open('out.csv', 'w', newline='') as csvout:
            csv_writer = csv.writer(csvout)
            for row in sorted_reader:
                csv_writer.writerow(row)


def demo_csv_dict():
    with open('test_file.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        sorted_reader = sorted(csv_reader, key=lambda x: x['age']) #don't use this if you don't want to print the sorted dict
        with open('out_dict.csv', 'w', newline='') as csvout:
            field_names = ['first','last','age','email']
            csv_writer = csv.DictWriter(csvout, fieldnames=field_names)
            csv_writer.writeheader()
            for line in sorted_reader:
                csv_writer.writerow(line)


def main():
    #demo_csv()
    demo_csv_dict()
    

if __name__ == "__main__":
    main()