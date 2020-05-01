Spisok = [3, 5, 7, 9, 10.5]
print(Spisok)
Spisok.append('Python')
print(Spisok)
print(Spisok[-1])

Spisok.remove('Python')
print(Spisok)


dic = {"city":"Москва", "temperature":"20"}
print(dic["city"])
dic["temperature"] = '15'
print(dic)
print(dic.get("country"))
dic["country"] = "Россия"
print(dic)
dic["data"] = "27.05.2019"
print(dic)
print(len(dic))