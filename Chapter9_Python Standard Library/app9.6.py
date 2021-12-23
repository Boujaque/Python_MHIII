# 6 -  Working with CSV files
import csv

# file = open("data.csv", "w")
# file.close()

# better approach
# writting to CSV
# with open("data.csv", "w")as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([100, 1, 5])
#     writer.writerow([101, 2, 15])

# reading from CSV
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
# iterare over the reader
    for row in reader:
        print(row)
