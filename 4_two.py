import sys
def open_file(arg1,arg2):
  try:
    file_one=open(arg1,arg2)
  except:
    print "file not found"
  return file_one

def logic():

  count=0
  input_file=open_file(sys.argv[1],"r") 
  output_file=open_file(sys.argv[2],"w")
  for line in input_file:
    if count==0:
      header_output=line
      header_output=header_output.replace("\n","")
      header_output=header_output+",Sales_Tax,Final_Price \n"
      output_file.write(header_output)
      count=count+1
    else:
      line=line.replace("\n","")
      data=line.split(",")
      data=data[2]
      price=int(data)*18
      price /=100
      final_price=price+int(data)
      line=line+","+str(price)+","+str(final_price)+"\n"
      output_file.write(line)
def main():
  try:
    logic()
  except:
    ""
main()

