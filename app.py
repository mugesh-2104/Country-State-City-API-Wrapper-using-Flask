from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COUNTRIES_API = "https://countriesnow.space/api/v0.1/countries"
STATES_API = "https://countriesnow.space/api/v0.1/countries/states"
CITIES_API = "https://countriesnow.space/api/v0.1/countries/state/cities"

@app.route('/getallcountries')
def get_all_countries():
    response = requests.get(COUNTRIES_API)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch countries"}), 500

    countries = response.json().get("data", [])
    country_list = [country["country"] for country in countries]
    return jsonify({"countries": country_list})

@app.route('/getstates')
def get_states():
    country = request.args.get("country")
    if not country:
        return jsonify({"error": "Missing 'country' parameter"}), 400

    response = requests.post(STATES_API, json={"country": country})
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch states"}), 500

    states = response.json().get("data", {}).get("states", [])
    state_list = [state["name"] for state in states]
    return jsonify({"states": state_list})

@app.route('/getcities')
def get_cities():
    country = request.args.get("country")
    state = request.args.get("state")
    if not country or not state:
        return jsonify({"error": "Missing 'country' or 'state' parameter"}), 400

    response = requests.post(CITIES_API, json={"country": country, "state": state})
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch cities"}), 500

    cities = response.json().get("data", [])
    return jsonify({"cities": cities})

if __name__ == '__main__':
    app.run(port=3000, debug=True)
