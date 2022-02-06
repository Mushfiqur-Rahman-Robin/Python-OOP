import json
from textwrap import indent

python_string  = '''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "area_codes": ["205", "251", "256", "334", "938"]
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "area_codes": ["907"]
    }
  ]
}

'''

data = json.loads(python_string)
#print(data)

# Performs the following translations in decoding by default:

# JSON          Python

# object        dict

# array         list

# string        str

# number(int)   int

# number(real)  float

# true          True

# false         False

# null          None

print(type(data['states']))  # <class 'list'>

for state in data['states']:
    #print(state)
    pass


# dumping a python object to a json string

for state in data['states']:
    del state['area_codes']

new_str = json.dumps(data, indent = 2, sort_keys=True)
#print(new_str)

# load json files into python objects and write those objects back to json files

# load method loads a file into a python object
# loads methods loads a string

with open(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer's Python in-depth tutorial\states.json") as f:
    data = json.load(f)

for state in data['states']:
    #print(state)
    #print(state['name'], state['abbreviation'])
    del state['area_codes']

with open(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer's Python in-depth tutorial\updated_states.json", 'w') as f:
    json.dump(data, f, indent = 2)


import json
from urllib.request import urlopen

with urlopen("https://quantprice.herokuapp.com/api/v1.1/scoop/day?tickers=MSFT&date=2017-06-09") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))


# This code is copied from Corey Schafer's github repo
# May help for real world use cases
# This API doesn't function currently

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))