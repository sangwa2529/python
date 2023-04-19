import json
file = open("file.json","r")
x = file.read()
finaldata=json.loads(x)

for a in finaldata:
    print(a['id'],"Name: ", a['first_name'], a['last_name'])
    print("Email: ",  a['email'])
    print("Gender: ",  a['gender'])
    print("IP Address: ", a['ip_address'])
    print()



