import sys

class Sales:
  
  def __init__(self):
    try:
      self.input_file=self.open_file(sys.argv[1],"r") 
      self.output_file=self.open_file(sys.argv[2],"w")
    except:
      print "file not found"
    else:
      self.logic()

    
  def open_file(self,arg1,arg2):
    
    return open(arg1,arg2)
    
  def read(self):
    self.data=self.input_file.readlines()

  def write(self,temp):
    self.output_file.write(temp)

  def sales_tax_cal(self,temp):
    price=int(str(temp))*18
    price /=100
    return price

  def final_price_cal(self,price,sales):
    return price+sales


  def logic(self):
    self.read()
    self.write(str(self.data[0]).replace("\n","")+",Sales_Tax,Final_price\n")
    self.data.remove(self.data[0])
    index=0
    while(index<len(self.data)-1):
      temp=str(self.data[index])
      temp=temp.split(",")
      price=temp[2]
      sales=self.sales_tax_cal(price)
      final_price=self.final_price_cal(int(str(price)),int(str(sales)))
      self.write(str(self.data[index]).replace("\n","")+","+str(price)+","+str(final_price)+"\n")
      index=index+1

sale1=Sales()




