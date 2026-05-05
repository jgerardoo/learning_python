# Read a file content
## Read the (whole) file
with open("files/first_file.txt") as first_file:
    print(first_file.read())
print("--------------------")

## Read the file in lines
with open("files/first_file.txt") as first_file:
    for line in first_file.readlines():
        print(line)
print("--------------------")

## Read a single line at a time
with open("files/first_file.txt") as first_file:
    first_line = first_file.readline()
    second_line = first_file.readline()
    print(second_line)
print("--------------------")

## Write a file
with open("files/music_bands.txt", "w") as music_bands_doc:
  music_bands_doc.write("Soda Stereo")

## Appending to a file
with open("files/music_bands.txt", "a") as music_bands_doc:
    music_bands_doc.write("\nLinkin Park")

## Reading a CSV File
import csv

with open("files/cool_data.csv") as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row["Cool Fact"])
print("--------------------")

## Create a list from a CSV file
list_of_fun_facts = []
with open("files/cool_data.csv", newline = "") as cool_csv_file:
    fun_facts = csv.DictReader(cool_csv_file)
    for row in fun_facts:
        list_of_fun_facts.append(row["Cool Fact"])
print(list_of_fun_facts)
print("--------------------")

# Reading Different Types of CSV Files
## you have to specify the delimiter of the data
## the delimiter in "books.csv" file is '@'
title_list = []
authors_list = []
isbn_list = []
with open("files/books.csv") as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter = '@')
    for row in books_reader:
        title_list.append(row["Title"])
        authors_list.append(row["Author"])
        isbn_list.append(row["ISBN"])
print(title_list)
print(authors_list)
print(isbn_list)
print("--------------------")

# Writing a CSV file from data in python
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open("files/logger.csv", "w") as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
    log_writer.writeheader()
    for item in access_log:
        log_writer.writerow(item)
## this code wrote the info from the lists into the logger.csv file

# Read a JSON file
import json

with open('files/message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])
  print(message['secret text'])
print("--------------------")

# Writing a JSON file
data_payload = {"interesting message": "What is JSON? A web application's little pile of secrets.", "follow up": "But enough talk!"}
with open("files/data.json", "w") as data_json:
  json.dump(data_payload, data_json)
## this code created a new json file named :data.json" and wrote the info from the list into the file

# 