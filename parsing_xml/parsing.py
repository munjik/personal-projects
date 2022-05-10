import requests
import xml.etree.ElementTree as ET
import xmltodict, json


# url = 'https://www.washingtonpost.com/arcio/news-sitemap/'


url = 'http://api.worldbank.org/countries'
response = requests.get(url)
root = ET.fromstring(response.content)
namespaces = {'wb': "http://www.worldbank.org"}

code_list = []
name_list = []
region_list = []
adminregion_list = []
incomeLevel_list = []
lendingType_list = []
capitalCity_list = []
longitude_list = []
latitude_list = []

# print(root.tag)
# print(root.attrib)
# for element in root.iter():
#     print(element.tag, element.text)
myDict = dict()

for country in root.findall('wb:country', namespaces):
    code = country.find('wb:iso2Code', namespaces).text
    name = country.find('wb:name', namespaces).text
    region = country.find('wb:region', namespaces).text
    adminregion = country.find('wb:adminregion', namespaces).text
    incomeLevel = country.find('wb:adminregion', namespaces).text
    lendingType = country.find('wb:lendingType', namespaces).text
    capitalCity = country.find('wb:capitalCity', namespaces).text
    longitude = country.find('wb:longitude', namespaces).text
    latitude = country.find('wb:latitude', namespaces).text

    code_list.append(code)
    name_list.append(name)
    region_list.append(region)
    adminregion_list.append(adminregion)
    incomeLevel_list.append(incomeLevel)
    lendingType_list.append(lendingType)
    capitalCity_list.append(capitalCity)
    longitude_list.append(longitude)
    latitude_list.append(latitude)

# create a dictionary to convert into JSON. Format will match the orignal XML.
# create empty dict
nodes = {}
for a, b, c, d, e, f, g, h, i in zip(code_list, name_list, region_list, adminregion_list, incomeLevel_list, lendingType_list, capitalCity_list, longitude_list, latitude_list):
    # code_list[a][name_list] = {'code_list': a, 'name_list': b, 'region_list':c ,'adminregion_list': d, 'incomeLevel_list': e,
    #                                'lendingType_list': f, 'capitalCity_list': g, "longitude_list": h,"latitude_list" : i}
    nodes[a] = {
        'iso2Code': a,
        "country_name" : b,
        'region' : c,
        'adminregion': d,
        'incomelevel': e,
        'lendingtype': f,
        'capitalCity': g,
        'longitude' : h,
        'latitude' : i
    }
# array = [{'key': i, 'value' : nodes[i]} for i in nodes]

# json.dumps take a dictionary as input and returns a string as output.
final_json = json.dumps(nodes)

# write to a file
with open("countries.json","w") as f:
  f.write(final_json)

# reads it back
with open("countries.json","r") as f:
  data = f.read()

# decoding the JSON to dictionay
d = json.loads(data)

print(d['AW']['region'])
