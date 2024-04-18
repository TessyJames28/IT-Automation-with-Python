import csv

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

key = ["name", "username", "department"]
with open("by_department.csv", "w") as department:
    writer = csv.DictWriter(department, fieldnames=key, lineterminator="\n")
    writer.writeheader()
    writer.writerows(users)