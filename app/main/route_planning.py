
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBainUCQKRqOgSDsXOtYqpQDo4gv4fRwQE')

#short form of address, such as country + postal code
geocode_result = gmaps.geocode('singapore 018956')

#full address
geocode_result = gmaps.geocode("10 Bayfront Ave, Singapore 018956")

#a place name
geocode_result = gmaps.geocode("zhongshan park")

#Chinese characters
geocode_result = gmaps.geocode('滨海湾花园')

#place name/restaurant name
geocode_result = gmaps.geocode('jumbo seafood east coast')

print(geocode_result[0]["formatted_address"]) 
print(geocode_result[0]["geometry"]["location"]["lat"]) 
print(geocode_result[0]["geometry"]["location"]["lng"])

reverse_geocode_result = gmaps.reverse_geocode((1.3550021,103.7084641))

print(reverse_geocode_result[0]["formatted_address"])
#'87 Farrer Dr, Singapore 259287'

#GETTING DISTANCES
from datetime import datetime, timedelta

gmaps.distance_matrix(origins=geocode_result[0]['formatted_address'], 
                      destinations=reverse_geocode_result[0]["formatted_address"], 
                      departure_time=datetime.now() + timedelta(minutes=10))