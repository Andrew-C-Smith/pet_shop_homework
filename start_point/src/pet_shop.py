# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]


def add_or_remove_cash(total_new_cash ,cash):
    total_new_cash["admin"]["total_cash"] += cash
    return total_new_cash
    

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(new_sold, sold):
    new_sold["admin"]["pets_sold"] += sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    list_of_pets = []
   
    pets = pet_shop["pets"]
   
    for pet in pets:
            if pet["breed"] == breed:
                list_of_pets.append(pet)
   
    return list_of_pets



def find_pet_by_name(pet_shop, pet_name):
   
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
           
            return pet


def remove_pet_by_name(pet_shop, pet_name):
  
    for pet in pet_shop["pets"] :
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)  


def add_pet_to_stock(pet_shop, new_pet):
    return pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"]) 

def add_pet_to_customer(customer, new_pet):
    return customer["pets"].append(new_pet)

# optional tests

def customer_can_afford_pet(customer, new_pet):

    if customer["cash"] >= new_pet["price"]:
        return True
    else: return False


def sell_pet_to_customer(pet_shop, pet, customer):

    

   

