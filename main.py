import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
home_link = "https://www.99restaurants.com/"
response = requests.get(home_link)

# Check for the "Cache-Control" header
#cache_control = response.headers.get('Cache-Control')
#print(f"Cache-Control header: {cache_control}")

# Save the response content to a file
with open('cache_site.html', 'wb') as fh:
    fh.write(response.content)

# Parse the response content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
checks = soup.find_all('a', class_ = "location-address")
print(checks)
