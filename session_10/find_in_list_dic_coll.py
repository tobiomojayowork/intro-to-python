my_places = []

my_places.append(
    {
        "town": "Sharm-El-Sheikh", 
        "country": "Egypt", 
        "year": 2012, 
        "enjoyed": False
    }
)

my_places.append(
    {
        "town": "Phuket", 
        "country": "Thailand", 
        "year": 2019, 
        "enjoyed": True
    }
)

my_places.append(
    {
        "town": "Bali", 
        "country": "Indonesia", 
        "year": 2020, 
        "enjoyed": True
    }
)

my_places.append(
    {
        "town": "Gran Canaria", 
        "country": "Spain", 
        "year": 2018, 
        "enjoyed": False
    }
)

my_places.append(
    {
        "town": "Gran Canaria", 
        "country": "Spain", 
        "year": 2022, 
        "enjoyed": False
    }
)

my_places.append(
    {
        "town": "Rethynmo", 
        "country": "Crete", 
        "year": 2022, 
        "enjoyed": False
    }
)

my_places.append(
    {
        "town": "Rethynmo", 
        "country": "Crete", 
        "year": 2022, 
        "enjoyed": False
    }
)

my_places.append(
    {
        "town": "Agadir", 
        "country": "Morocco", 
        "year": 2023, 
        "enjoyed": False
    }
)


def IsKeyPairInDicColl(coll_list_dic, keyName, keyValue):
    # this only works for a list collection containing dictionary items: [{....}, {}, ...]

    exists = False

    for item in coll_list_dic:
        if keyName in item and item[keyName]==keyValue:
            print(f'{keyName}={item[keyName]} exists')        


IsKeyPairInDicColl(my_places, "year", 2022)
