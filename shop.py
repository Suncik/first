class SuperClass:
    def __init__(self, model, price):
        self.model=model
        self.price=price
            






class Tv(SuperClass):
    def __init__(self, model, price, size):
        super().__init__(model, price)   
        self.size=size
        self.type="tv"
    def info_TV(self):
               print(f"model: {self.model}, price:{self.price}, size:{self.size}")
        #  ===================PC===============
class PC(SuperClass) :
    def __init__(self, model, price, cpu):
        super().__init__(model, price)
        self.cpu=cpu
        self.type="pc" 
    
    def info_PC(self):
               print(f"model: {self.model}, price:{self.price}, cpu:{self.cpu}")
        
t1=Tv("artel", 300, "42")
t2=Tv("lg", 400, "72")     
p1=PC("dell", 1300, 16)
p2=PC("mac", 2300, 16)  

#            =============== SHOP===========                   

                               
class Shop:
    def __init__(self, title, phone):     
        self.title=title  
        self.phone=phone
        self.data_PC=[]  
        self.data_TV=[]            
        
    def add_product_TV(self):   
        model=input(f"model:")
        price=input(f"price:")
        size=input(f"size:")
        pro=Tv(model, price, size)
        self.data_TV.append(pro)                 
        
    def add_product_PC(self):
          model=input(f"model:")
          price=input(f"price:")
          cpu=input(f"cpu:")
          pro=PC(model, price, cpu)         
          self.data_PC.append(pro)              
        

        
    def view_products(self): 
        
        
        kod=input("1.tv views \n 2.pc views")  
        if kod=="1":
            for item in self.data_TV:
                item.info_TV()                    
        elif kod=="2":
            for item in self.data_PC:
                item.info_PC()
        
            
                
                
        
        
s1=Shop("shop1", "+211")   
s2=Shop("shop2", "+221211") 
baza=[s1, s2]         
s1.data_TV=[t1,t2]    
s1.data_PC=[p1,p2]


def add_shop():
    title=input("title:")
    phone=input("phone:")
    s3=Shop(title, phone)     
    baza.append(s3) 
    
def view_data():
    for item in baza:
        print(f"title:{item.title}, phone:{item.phone}")

def delete_shop():
    sh=input("shopName:")
    for item in baza:
        if item.title==sh:
            baza.remove(item)
            
def shop_manager(shop: Shop):                        
        while True:
            kod=input(f"1.add tv \n 2.add pc \n 3.view products \n 4.exit")
            if kod=="1":
                shop.add_product_TV()
            elif kod=="2":         
                shop.add_product_PC()
            elif kod=="3": 
                shop.view_products()
            else:
                break
# shop_manager(s1)
            
   
                
            


def shops_manager(): 
    while True:
        kod=input("1.add shop \n 2.view shop \n 3.dell shop \n 4.exit:")
        if kod=="1":
            add_shop()  
        elif kod=="2":
            view_data()
            index=input("shop number:")
            if index=="1":  
                 shop_manager(s1)
            else: shop_manager(s2)
                
            
        elif kod=="3":
            delete_shop()
        elif kod=="4": exit()
        
shops_manager()   