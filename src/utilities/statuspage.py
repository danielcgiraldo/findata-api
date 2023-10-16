import requests
import os
# Load environment variables from the .env file


# Define your page_id and API key
page_id = os.getenv("STATUSPAGE_PAGE_ID")
api_key = os.getenv("STATUSPAGE_API_KEY")

# Define the incident data
incident_data = {
    "incident[name]": "Incidente de prueba",
    "incident[status]": "identified",
    "incident[body]": "Este es un incidente de prueba",
    "incident[impact_override]": "minor",
    "incident[component_ids]": ["h01x51wdstl5"],
    "incident[components][h01x51wdstl5]": "major_outage"

}

# Define the API endpoint URL
url = f"https://api.statuspage.io/v1/pages/{page_id}/incidents"

# Define headers with the Authorization token
headers = {
    "Authorization": f"OAuth {api_key}"
}

# Send a POST request to create the incident
response = requests.post(url, headers=headers, data=incident_data)

# Check the response status
if response.status_code == 201:
    print("Incident created successfully")
else:
    print(f"Failed to create incident. Status code: {response.status_code}")
    print(response.text)
