import csv
import sys
import webbrowser

try:
    file = sys.argv[1] 
except IndexError:
    print("No file dropped")

with open(file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    next(csv_reader)

    url = "https://resourcecalculator.com/minecraft/#"

    for row in csv_reader:
        url += row[0].lower().replace(" ", "")
        url += "="
        url += row[1]
        url += "&"

url.rstrip("&")
webbrowser.open_new(url)
