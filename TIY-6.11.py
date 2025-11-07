# Date: 11 november 2025
# Name: Riyyan

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.


cities = {'Lahore':{'country':'Pakistan',
                    'population':'13 milion',
                    'fact':'cultural heart of Pakistan'}
          ,'Islamabad':{'country':'Pakistan',
                    'population':'1.1 milion',
                    'fact':'planned city that became the capital of Pakistan'},
            'Karachi':{'country':'Pakistan',
                    'population':'18 milion',
                    'fact':'largest city in Pakistan'},}

for city, facts in cities.items():
    print(f"{city}: ".title())
    for fact,detail in facts.items():
        print(f"  {fact}: {detail}".title())