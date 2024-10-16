# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:52:37 2024

@author: emrec
Use of quote_plus
"""

from urllib.parse import quote_plus

# Example parameters, change them
params = {
    "name": "John Doe",
    "city": "New York",
    "query": "ice cream & chocolate"
}

# Encode each parameter
encoded_params = "&".join([f"{key}={quote_plus(value)}" for key, value in params.items()])

# Construct URL
url = f"https://www.example.com/search?{encoded_params}"

print(url)