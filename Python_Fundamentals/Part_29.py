# COPY & POP DICTIONARY

teman_teman = {
    "kr": "krisna ganteng",
    "do": "dominik ganteng",
    "her": "herlambang ganteng",
    "di": "dia cantik",
    "na": "nada cantik"
}

# copy dictionary
friends = teman_teman.copy()
print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

teman_teman["kr"] = "krisna cakep bet"
print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

# pop dictionary
dataDo = friends.pop("do")
print(f"data dominik = {dataDo}\n")
print(f"friends = {friends}\n")

# popitem dictionary
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")
