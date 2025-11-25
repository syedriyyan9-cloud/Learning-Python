def get_city_country_names(city, country,popluation=0):
    '''returns city country name in format of City, Country'''
    if popluation:
        return f"{city}, {country} - Population {popluation}".title()
    else:
        return f"{city}, {country}".title()

