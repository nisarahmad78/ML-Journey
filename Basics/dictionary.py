person = {"name" : "Nisar Ahmad", "age":16}
print(person['name'])
print(person.get("age"))

sum = person.get("age")+5
print(f"The addition of 5 now age is {sum}")


key = ["name", "age"]
values = ["Nisar", 25]

result = dict(zip(key, values))
print(result)