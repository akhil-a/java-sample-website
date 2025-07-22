import os
import sys
import requests

 #curl -s "https://hub.docker.com/v2/repositories/akhilanilkumar10/java-web-app/tags?page_size=100"

username="akhilanilkumar10"
image_name="java-web-app"
docker_api_url=f"https://hub.docker.com/v2/repositories/{username}/{image_name}/tags?page_size=100"


response = requests.get(docker_api_url)
response.raise_for_status()
data=response.json()
tag_list={}
for val in data['results']:
    tag_list[val['name']] = val['last_updated'].split('T')[0]

print(tag_list)


