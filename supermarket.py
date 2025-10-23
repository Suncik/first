from itertools import product


class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price



class Supermarket:
    def __init__(self):

        self.data=[
            Product("olma", 10),
            Product("burger", 20),
            Product("uzum", 30),
            Product("sabzi", 40),
            Product("olcha", 50),
            Product("o'rik", 60),
            Product("shaftoli", 70),
             Product("kartoshka", 80)
        ]


    def Add_product(self):
        product_name=input("Enter product name: ")
        price=input("Enter price: ")
        prn=Product(product_name, price)
        self.data.append(prn)

    def Print_products(self):
        i=0
        for prn in self.data:
            i+=1
            print(f"{i}.{prn.product_name}, {prn.price}")

    def remove_product(self ):
        pr_name=input("Enter product name: ")
        for prn in self.data:
            if prn.product_name==pr_name:
                self.data.remove(prn)

    def Edit_product(self):
        pr_name=input("Enter product name: ")
        for prn in self.data:
            if prn.product_name==pr_name:
                prn.price=input("Enter price: ")

    def control_market(self ):
        while True:
             kod=int(input("choose:\n 1.print products\n 2.remove product\n 3.Edit product \n 4.Exit"))
             if kod==1:
               self.Print_products()
             elif kod==2:
                self.remove_product()
             elif kod==3:
                     self.Edit_product()
             elif kod==4:
                break

class Customer():
    def __init__(self,username,password, market):
        self.username=username
        self.password=password
        self.market=market
        self.savat=[]


    def purchase(self):
      self.market.Print_products()
      pr=input("Enter product name: ")
      for item in self.market.data:
          if item.product_name.lower() == pr.lower():
              self.savat.append(item)
              self.market.data.remove(item)
              self.market.Print_products()
              print(f"{pr} savatga qo‘shildi ✅")
              break
      else:
          print("Mahsulot topilmadi ❌")







    def view_savat(self):
        for item in self.savat:
            print(item.product_name, item.price)



    def control_byCustomer(self ):
        while True:
            kod=int(input("choose:\n 1.purchase\n 2.view\n 3.Exit"))
            if kod==1:
                ob.purchase()
            elif kod==2:
                ob.view_savat()
            elif kod==3:
                break












b=Supermarket()
market=Supermarket()
ob=Customer("suncik", "1111", market)

while True:
    kod=int(input("choose:1.Admin \n 2.user \n 3.Exit "))
    if kod==1:
        parol=input("parol:")
        if parol=="1234":
            b.control_market()
        else: print("failed")
        break
    elif kod==2:
        ob.control_byCustomer()
    elif kod==3:
        break













