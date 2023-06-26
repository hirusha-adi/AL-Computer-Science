import requests

# GraphQL API URL
url = 'https://api.apluseducation.lk/api/gql'

# GraphQL query
query = '''
    query {
      getSysInfo {
        canPlaceStudentPayment
      }
    }
'''

# Send the GraphQL request
response = requests.post(url, json={'query': query})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract the information from the response
    sys_info = data['data']['getSysInfo']
    can_place_payment = sys_info['canPlaceStudentPayment']

    # Print the retrieved information
    print(f"Can place student payment: {can_place_payment}")
else:
    print(f"Request failed with status code {response.status_code}")
