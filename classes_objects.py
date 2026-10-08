""""
class Book:
    def __init__(self, title, author, pages): 
        self.title = title 
        self.author = author 
        self.pages = pages 

    def show_info(self): 
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"pages: {self.pages}")


Book1 = Book("Kan inga böcker", "Frans", 10000)

Book1.show_info()

"""

"""""
class Phone: 
    def __init__(self, brand, model, color, battery, storage):
        self.brand = brand
        self.model = model  
        self.color = color
        self.battery = battery
        self.storage = storage

    def show_status(self):
        print("Phone:", self.brand)
        print("Phone:", self.model)
        print("Phone:", self.color)
        print("Phone:", self.battery)
        print("Phone:", self.storage)
        

Phone1 = Phone("Apple", "Iphone 18 pro", "Black", "100%", "128GB")
Phone1.show_status()

"""

class TemperatureSensor:
    def __init__(self, location, temperature, ):
        self.loaction = location
        self.temperature = temperature

    def show_status(self):
        print("TemperatureSensor:", "self.location:")
        print("Temperature:", "self.temperature:")

TemperatureSensor1 = TemperatureSensor("Sovrum", "22 grader")
TemperatureSensor1.show_status()

