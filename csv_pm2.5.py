import csv

file = open('', 'w', newline = None)

csvwriter = csv.writer(file, delimiter=',')

csvwriter.writerow(["PM2.5"])

file.close()
