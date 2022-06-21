# dictionaries - use key value pairs
abby_dict = {"f_name": "Abby", "l_name": "Baker", "address": "123 Main Street"}

print(abby_dict["f_name"])

abby_dict["address"] = "215 North St"
abby_dict["city"] = "Pittsburgh"
print("Is there a city?", "city" in abby_dict)
print(abby_dict.values())
print(abby_dict.keys())

for k, v in abby_dict.items():
    print(k, v)

print(abby_dict.get("m_name", "not here"))
del abby_dict["f_name"]
for i in abby_dict:
    print(i)

abby_dict.clear()

# employees = []
# f_name, l_name = input("enter employee name: ").split()
# employees.append({"f_name": f_name, "l_name": l_name})
# print(employees)

# create an array of customer dictionaries
# sample output:
# enter customer (y/n): y
# enter customer name: abby baker
# enter customer (y/n): y
# enter customer name: matthew hudson
# enter customer (y/n): n
# abby baker
# matthew hudson
customers = []
while True:
    response = input("enter customer (y/n): ").lower().strip()
    response = response[0]
    if response == "n":
        break
    else:
        f_name, l_name = input("enter customer first and last name: ").lower().split()
        customers.append({"f_name": f_name, "l_name": l_name})

for cust in customers:
    print(cust["f_name"], cust["l_name"])

