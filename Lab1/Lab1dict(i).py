#Use dir and help to learn about the functions you can call on dictionaries and implement it. 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2=thisdict.copy()
print(thisdict2)
print(thisdict.get("brand"))
print(thisdict.items())
print(thisdict.keys())
thisdict.pop("year")
print(thisdict)
thisdict.popitem()
print(thisdict)
print(thisdict.setdefault("brand"))
print(thisdict.values())
thisdict.update({"year":"1964"})
print(thisdict)
x=("price")
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
thisdict.clear()
print(thisdict)