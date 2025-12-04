#collection of {key:value} pairs
#ordered and changeable.No duplicates

capitals={"USA":"Washington D.C",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"
          }

print(capitals)
print()
print(capitals.get("USA"))

if capitals.get("Japan"):
    print("Exist")
else:
    print("Does'nt")
print("===============================================================================================")
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Alabama"})
capitals.pop("China")
capitals.popitem()#latest key value pair popped
# capitals.clear()

print(capitals)
print("===============================================================================================")
keys=capitals.keys()
# print(keys)

for key in capitals.keys():
    print(key)
print("===============================================================================================")
values=capitals.values()
# print(values)

for value in capitals.values():
    print(value)
print("===============================================================================================")
#Items

items=capitals.items()
# print(items)
for key,value in capitals.items():
    print(f"{key}: {value}")