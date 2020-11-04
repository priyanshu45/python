#dictionary method in pyton referance are available on visit-https://www.w3schools.com/python/python_ref_dictionary.asp
#dictionary method
# Dictionary is pair of keys in python.
#  d1 = {}
# print(type(d1))
d2 = {"priyanshu":"samosa",
      "cat":"billi",
      "Ram":"god",
      "Manish":"Priyanshu",
      "sbi":  {"mohan": "nahihai","L":"roti" },
 "shayam":{"j":"atta maggie", "p":" nan roti", "l":"Chicken leg piece"}
      }
d2["aman"] = "junk food"
# print(d2)
del d2["cat"]
d3 = d2.copy()
# print(d3)
# d2.update({"cam":"mam"})
# print(d2)
#print(d2.keys())
#print(d2.items())
                             #finding words in python dictionary.
print(d2['aman'])