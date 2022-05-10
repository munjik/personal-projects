import requests
import xml.etree.ElementTree as ET
import xmltodict, json

url = 'https://www.washingtonpost.com/arcio/news-sitemap/'
response = requests.get(url)
root = ET.fromstring(response.content)

namespaces = {'urlset': "http://www.sitemaps.org/schemas/sitemap/0.9"}
news_namespaces = {'urlset': 'http://www.google.com/schemas/sitemap-news/0.9'}


for pubs in root.findall('urlset:url', namespaces):
    location = pubs.find('.//{*}loc', namespaces).text
    modification = pubs.find('.//{*}lastmod',namespaces).text
    news = pubs.find('.//{*}news', namespaces)
    for new in news:
        print(new)
    change = pubs.find('.//{*}changefreq', namespaces).text


# root = ElementTree.fromstring(response.text)

# namespaces = {
#     "_": "http://www.sitemaps.org/schemas/sitemap/0.9",
#     "news": "http://www.google.com/schemas/sitemap-news/0.9",
#     "video": "http://www.google.com/schemas/sitemap-video/1.1",
# }

# for pubs in root.findall('_:url', namespaces):
#     news_items = pubs.findall('news:news', namespaces)
#     for news_item in news_items:
#         print(news_item)
#         for news_publication in news_item.findall('news:publication', namespaces):
#             print('    ' + str(news_publication))
