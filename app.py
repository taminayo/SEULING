from result import Result
import requests
import csv

with open('raw.csv', 'r') as raw:
	csv_reader = csv.DictReader(raw)
	raw_fieldname = csv_reader.fieldnames[0]
	with open('edited.csv', 'w') as edited:
		fieldnames = [csv_reader.fieldnames[0], '상태']
		
		csv_writer = csv.DictWriter(edited, fieldnames=fieldnames)
		csv_writer.writeheader()
		for line in csv_reader:
			num, status = Result(line[raw_fieldname]).getStatus()
			csv_writer.writerow({fieldnames[0]:num, fieldnames[1]:status})
