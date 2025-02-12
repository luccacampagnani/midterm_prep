d = {}
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "español"

print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])

eng_to_spa.update({"yes": "si", "no": "no"})
print(eng_to_spa)
del eng_to_spa["no"]
print(eng_to_spa)

print(eng_to_spa.pop("two")) #deletes two and dos from dictionary

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")

print(eng_to_spa.get("tree", "unknown value"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

for key, value in eng_to_spa.items():
    print(f"{value} means {key}")