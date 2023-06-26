import requests

# API endpoint URL
url = 'https://api.apluseducation.lk/api/gql'

# GraphQL query
query = '''
  query {
    appInfo {
      apiName
      apiVersion
      storageBucketVideoRoot
      storageBucketImageRoot
    }
  }
'''

# Send POST request
response = requests.post(url, json={'query': query})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract relevant information from the response
    app_info = data['data']['appInfo']
    api_name = app_info['apiName']
    api_version = app_info['apiVersion']
    storage_bucket_video_root = app_info['storageBucketVideoRoot']
    storage_bucket_image_root = app_info['storageBucketImageRoot']

    # Print the retrieved information
    print(f"API Name: {api_name}")
    print(f"API Version: {api_version}")
    print(f"Storage Bucket (Video Root): {storage_bucket_video_root}")
    print(f"Storage Bucket (Image Root): {storage_bucket_image_root}")
else:
    print(f"Request failed with status code {response.status_code}")
