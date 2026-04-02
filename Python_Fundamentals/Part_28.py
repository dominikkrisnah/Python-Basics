# LOOPING DICTIONARY

teman_teman = {
    "kr": "krisna ganteng",
    "do": "dominik ganteng",
    "her": "herlambang ganteng",
    "di": "dia cantik",
    "na": "nada cantik"
}

# looping first try
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman:
    print(teman_teman.get(key))

valuess = teman_teman.values()
print(valuess)

for value in teman_teman.values():
    print(value)

itemsku = teman_teman.items()
print(itemsku)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")
