import sys
sys.path.insert(0, './site-packages')

from result import Result
import requests
import csv
print(requests)

with open('raw.csv', 'r', encoding='UTF-8') as raw:
	csv_reader = csv.DictReader(raw)
	raw_fieldname = csv_reader.fieldnames[0]
	with open('edited.csv', 'w', encoding='UTF-8') as edited:
		fieldnames = [csv_reader.fieldnames[0], '상태']
		
		csv_writer = csv.DictWriter(edited, fieldnames=fieldnames, lineterminator='\n')
		csv_writer.writeheader()
		for line in csv_reader:
			num, status = Result(line[raw_fieldname]).getStatus()
			csv_writer.writerow({fieldnames[0]:num, fieldnames[1]:status})
