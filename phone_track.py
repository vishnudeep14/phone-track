import phonenumbers
from phonenumbers import geocoder
import folium

number = "+14842634790"
ch_num = phonenumbers.parse (number, "CH")
yourloc = (geocoder.description_for_number (ch_num, "en"))
from phonenumbers import carrier

serv_num = phonenumbers.parse (number, "RO")
print (carrier.name_for_number (serv_num, "en"))

key = "4f5ab13a32d446d0a841533d52d20518"
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode (key)
query = str (yourloc)
results = geocoder.geocode (query)
print (results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

mym = folium.Map (location=[lat, lng], zoom_start_=9)
folium.Marker ([lat, lng], popup=yourloc).add_to (mym)
print(lat,lng)

mym.save ("mylocn.html")

