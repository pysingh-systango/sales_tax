import csv
import sys
input_file=open(sys.argv[1],"rb")
reader=csv.reader(input_file)

for data in reader:
	print data

