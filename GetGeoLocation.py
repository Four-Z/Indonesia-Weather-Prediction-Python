# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

def getLatitude(location):
    getLoc = loc.geocode(location)
    return getLoc.latitude
    
def getLongtitude(location):
    getLoc = loc.geocode(location)
    return getLoc.longitude

def getAddress(location):
    getLoc = loc.geocode(location)
    print(getLoc.address)


