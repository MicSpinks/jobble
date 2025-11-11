from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time

def geocode_location(location_string):
    """
    Geocode a location string into coordinates and structured address.
    Returns dict with: latitude, longitude, city, state, country
    """
    if not location_string or not location_string.strip():
        return None
    
    try:
        geolocator = Nominatim(user_agent="jobble_app")
        # Add a small delay to avoid rate limiting
        time.sleep(1)
        
        location = geolocator.geocode(location_string, addressdetails=True)
        
        if location:
            address = location.raw.get('address', {})
            
            return {
                'latitude': location.latitude,
                'longitude': location.longitude,
                'city': address.get('city') or address.get('town') or address.get('village') or '',
                'state': address.get('state') or '',
                'country': address.get('country') or '',
                'display_name': location.address
            }
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding error: {e}")
        return None
    
    return None