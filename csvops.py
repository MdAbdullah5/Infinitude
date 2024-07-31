import csv
def print_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)  # Convert CSV reader object to list of lists

    max_lengths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        print(" | ".join(f"{item:<{length}}" for item, length in zip(row, max_lengths)))
# def print_table(data):
#     max_lengths = [max(len(str(item)) for item in col) for col in zip(*data)]
#     for row in data:
#         print(" | ".join(f"{item:<{length}}" for item, length in zip(row, max_lengths)))
def append_to_csv(filename, row):
    # 'a' mode is for appending (open file for writing, create it if it doesn't exist)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

row=[5,"Abdullah",22,10000]
append_to_csv("sample.csv",row)

print_csv_file("sample.csv")

with open("sample.csv",'r') as f:
    k=f.read()
    print(k)
