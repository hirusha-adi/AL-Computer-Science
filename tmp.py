import requests
import json

def query_graphql_api(url, query):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'query': query,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Replace 'https://api.apluseducation.lk/api/gql' with the actual GraphQL API endpoint URL
api_url = 'https://api.apluseducation.lk/api/gql'

# GraphQL query to retrieve all available endpoints
query = '''
    {
        __schema {
            queryType {
                fields {
                    name
                    description
                }
            }
        }
    }
'''

# Send the query to the API endpoint
response = query_graphql_api(api_url, query)

# Parse the response and store the endpoint information
endpoints = response['data']['__schema']['queryType']['fields']
result = ""

for endpoint in endpoints:
    name = endpoint['name']
    description = endpoint['description']
    result += f"Endpoint: {name}\n"
    result += f"Description: {description}\n\n"

# Save the results to a text file
filename = "endpoint_info.txt"

with open(filename, 'w') as file:
    file.write(result)

print(f"Results saved to {filename}.")
