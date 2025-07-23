import os
import sys
import requests

username="akhilanilkumar10"
image_name="java-web-app"
docker_api_url=f"https://hub.docker.com/v2/repositories/{username}/{image_name}/tags?page_size=100"



try:
    response = requests.get(docker_api_url)
    response.raise_for_status()
    data=response.json()
    tag_list={}
    for val in data['results']:
        tag_list[val['name']] = val['last_updated']

    if len(tag_list) >= 5:
        print("tag list are 5 or above")
        sorted_data = dict(sorted(tag_list.items(), key=lambda x: x[1], reverse=True))
        for tags in sorted_data:
            print(tags)
    else:
        print("less than 5")
except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
except KeyError as e:
        print(f"Missing expected data in response: {e}")
except Exception as e:
        print(f"An unexpected error occurred: {e}")


