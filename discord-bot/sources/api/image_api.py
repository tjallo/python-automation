"""
USING DUCKDUCKGO Search Engine
"""

import requests

def getHTML(query):
    query = query.replace(" ", "%20")
    URL = f"https://duckduckgo.com/?q={query}&atb=v241-4&iar=images&iax=images&ia=images"

    result = requests.get(URL)
    return result.text

print(getHTML("Klok bier"))