travel_log=[{
    "country":"iran",
    "visits":12,
    "cities":["tehran", "esfahan","shiraz"]},
    {
     "country":"france",
     "visits":40,
     "cities":["paris","monako","lille"]   
    }]
def add_new_country (new_country,new_visists,new_cities):
    new={}
    new["country"]=new_country
    new["visits"]=new_visists
    new["cities"]=new_cities
    travel_log.append(new)


add_new_country("russia", 14, ["mosco", "sanpitersborg"])
print(travel_log)
