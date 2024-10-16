# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13

@author: emre hosgor
Use of quote_plus
Small tasks
"""

from urllib.parse import quote_plus

# Example parameters, change them
params = {
    "name": "Emre Hosgor",
    "city": "New York",
    "query": "Admin & admin"
}

# Encode each parameter
encoded_params = "&".join([f"{key}={quote_plus(value)}" for key, value in params.items()])

# Construct URL
url_ = "https://www.example.com/search?"
url = f"{url_}{encoded_params}"

print(url)