from BasicHashTable import BasicHashTable

phone_numbers = {
    'Aakash' : '9489484949',
    'Hemanth' : '9595949494',
    'Siddhant' : '9231325312'
}
print(phone_numbers['Aakash'])
# you can put "Aakash" and change the value  
phone_numbers['Vishal'] = ' 8787878787'

# view the dictionary
print(phone_numbers)

hashtable = BasicHashTable()

hashtable.insert("new","table")
hashtable.insert("tank","shit")
hashtable.insert("arbies",123)


a = hashtable.find("arbies")
b = hashtable.get_index("tank")
print(a)
print(b)
