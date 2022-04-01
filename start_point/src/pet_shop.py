# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]


def add_or_remove_cash(total_new_cash ,cash ):
    total_new_cash["admin"]["total_cash"] +=cash
    return total_new_cash
    


   