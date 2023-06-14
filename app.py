from data import data


# INSTRUCTIONS
# 1) Split the full name into two fields, first name and last name

def split_name():
  for dictionary in data_clean:
    name_split = dictionary["name"].split()
    first_name = name_split[0]
    last_name = name_split[1]
    
    dictionary.update({"first_name":first_name})
    dictionary.update({"last_name":last_name})
    del dictionary["name"]

# 2) Convert the admin field to a boolean value

def convert_admin2boolean():
  for dictionary in data_clean:
    if dictionary["admin"].lower() == "false":
      dictionary["admin"] = bool("")
    else:
      dictionary["admin"] = bool("false")
    
# 3) Convert the id to an integer

def convert_id2int():
  for dictionary in data_clean:
    dictionary["id"] = int(dictionary["id"])

# 4) Keep the rest of the info the same
# 5) Complete this in a function(s)

def data_cleanser():
  split_name()
  convert_admin2boolean()
  convert_id2int()
  

# 6) Save the data into a new data structure: a list of dictionaries

data_clean = data.copy()
data_cleanser()
print(data_clean)
