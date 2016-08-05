import sys

input_file=sys.argv[1]
output_file=sys.argv[2]
try:
  file_one=open(input_file,"r")
except IOError:
  print "input file not found"
try:
  file_two=open(output_file,"w")
except IOError:
  print "cound't create output file"
count=0
for line in file_one:
 
  if count==0:
    header_output=line
    header_output=header_output.replace("\n","")
    header_output=header_output+",Sales_Tax,Final_Price \n"
    file_two.write(header_output)
    count=count+1
  else:
    line=line.replace("\n","")
    data=line.split(",")
    data=data[2]
    price=int(data)*18
    price /=100
    final_price=price+int(data)
    line=line+","+str(price)+","+str(final_price)+"\n"
    file_two.write(line)

