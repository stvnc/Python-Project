import requests
host = "https://developers.zomato.com/api/v2.1"
kategori = "/categories"

apikey = "56330392ccbb9e321437354a336ce0de"
headInfo = {
    "user-key":apikey
}

cityInput = input("Masukkan kota yang ingin dicari: ")
cities = f"/cities?q={cityInput}"
cityUrl = host + cities
city = requests.get(cityUrl, headers=headInfo)
cityCode = (city.json()["location_suggestions"][0]["id"])
menuInput = input("Makanan apa yang ingin anda cari : ")
menuUrl = host + f"/search?entity_id={cityCode}&entity_type=city&q={menuInput}"
data = requests.get(menuUrl, headers=headInfo)
data = (data.json()["restaurants"])
for i in range (len(data)):
    ambil = data[i]["restaurant"]
    print (f"+ {ambil['name']}, {ambil['location']['address']}, rating : {ambil['user_rating']['aggregate_rating']}")