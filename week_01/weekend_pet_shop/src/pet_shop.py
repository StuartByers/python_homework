# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, add_amount):
    cc_pet_shop["admin"]["total_cash"] += add_amount
    return None

def remove_cash(cc_pet_shop, remove_amount):
    cc_pet_shop["admin"]["total_cash"] -= remove_amount
    return None

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, increase_amount):
    cc_pet_shop["admin"]["pets_sold"] += increase_amount
    return None

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

# def get_pets_by_breed(cc_pet_shop, breed):
# Found

# def get_pets_by_breed(cc_pet_shop, breed):
# Not_Found

# def find_pet_by_name(cc_pet_shop, pet_name):
# Returns_Pet

# def find_pet_by_name(cc_pet_shop, pet_name):
# Returns_None
    
# def remove_pet_by_name(cc_pet_shop, removed_pet):

def add_pet_to_stock(cc_pet_shop, new_pet):
    return cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, removed_amount):
    customer["cash"] -= removed_amount
    return None

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    return customer["pets"].append(new_pet)
