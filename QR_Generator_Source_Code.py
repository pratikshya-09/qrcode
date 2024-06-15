
import random

import qrcode
import nepali_datetime

class Billing(): 
    pass

class FoodItems(): 
    def __init__(self, item_name='', weight=''):
        self.item_name = item_name
        self.weight = weight
        self.production_date = self.get_production_date()
    
    def display_info(self): 
        print(f"Name of Item: {self.item_name}")
        print(f"Weight: {self.weight} grams")
        print(f"Production Date: {self.production_date}")
        print("Best Use Before Six Months of Packaging")

    def gen_qr(self, filename="qr_code.png"): 
        data = {
            "Name of Item": self.item_name,
            "Weight": self.weight, 
            "Production Date": self.production_date,
            "Message": "Best Use Before Six Months"
        }
        qr_img = qrcode.make(data)
        qr_img.save(filename)

    def get_serial(self): 
        pass
    
    def get_production_date(self):
        date = nepali_datetime.date.today()
        return date

class Biscuit(FoodItems): 
    pass 

class Noodles(FoodItems): 
    pass

class Chips(FoodItems): 
    pass 

class Rice(FoodItems): 
    pass 

# Example usage
hamro = Biscuit('Hamro Biscuit', '100')
hamro.display_info()
hamro.gen_qr()
