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
    tag_list=[]
    for val in data['results']:
        list= []
        list.append(val['name'])
        list.append(val['last_updated'])
        tag_list.append(list)
    tag_list.sort(key=lambda x: x[1], reverse=True)
    tag_count=len(tag_list)
    print(f"Image : {username}/{image_name}")
    print("Tags : ")
    for tags in tag_list:
            print(f"{tags[0]}")
    if tag_count >= 5:
        print("Tags to delete :")
        for i in range(5,tag_count):
            print(tag_list[i])
        
    else:
        print("less than 5")
except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
except KeyError as e:
        print(f"Missing expected data in response: {e}")
except Exception as e:
        print(f"An unexpected error occurred: {e}")


