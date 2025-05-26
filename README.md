"""
Country-State-City API Wrapper using Flask
==========================================

📌 Description:
---------------
A lightweight Flask API wrapper over the CountriesNow public API.
Provides three endpoints:
    1. /getallcountries - List of all countries
    2. /getstates       - States in a given country
    3. /getcities       - Cities in a given state & country

⚙️ Technologies:
----------------
- Python 3.x
- Flask
- Requests
- External API: https://countriesnow.space/api/v0.1/

🧪 How to Run:
--------------
1. Install dependencies:
   pip install flask requests

2. Run the server:
   python app.py

3. Access API via:
   http://localhost:3000

📂 Endpoints:
-------------

1. GET /getallcountries
-----------------------
Returns a JSON list of all countries.

Example Request:
    GET http://localhost:3000/getallcountries

Example Response:
    {
        "countries": ["India", "USA", "Germany", ...]
    }

---

2. GET /getstates?country=CountryName
-------------------------------------
Returns a JSON list of all states for the specified country.

Required Query Param:
    - country (e.g., "India")

Example Request:
    GET http://localhost:3000/getstates?country=India

Example Response:
    {
        "states": ["Kerala", "Tamil Nadu", "Maharashtra", ...]
    }

---

3. GET /getcities?country=CountryName&state=StateName
------------------------------------------------------
Returns a JSON list of all cities for the specified state and country.

Required Query Params:
    - country (e.g., "India")
    - state   (e.g., "Kerala")

Example Request:
    GET http://localhost:3000/getcities?country=India&state=Kerala

Example Response:
    {
        "cities": ["Kochi", "Thiruvananthapuram", "Kozhikode", ...]
    }

👨‍💻 Author:
------------
Built by [Your Name] using the public CountriesNow API.
"""
