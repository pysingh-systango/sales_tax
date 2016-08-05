import sys

class Sales:
  
  
  def __init__(self):
    self.input_file=self.open_file(sys.argv[1],"r") 
    self.output_file=self.open_file(sys.argv[2],"w")
    
    
    
  def open_file(self,arg1,arg2):
    try:
      file_one=open(arg1,arg2)
    except IOError:
      print "file not found"
    return file_one

  def logic(self):
    
    data=self.input_file.readlines()
    self.output_file.write(str(data[0]).replace("\n","")+",Sales_Tax,Final_price\n")
    data.remove(data[0])
    index=0
    while(index<len(data)-1):
      temp=str(data[index])
      temp=temp.split(",")
      price=temp[2]
      price=int(str(price))*18
      price /=100
      final_price=int(str(temp[2]))+int(str(price))
      self.output_file.write(str(data[index]).replace("\n","")+","+str(price)+","+str(final_price)+"\n")
      index=index+1

sale1=Sales()
sale1.logic()



