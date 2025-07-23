import os
import sys
import requests

username="akhilanilkumar10"
image_name="java-web-app"
docker_list_url=f"https://hub.docker.com/v2/repositories/{username}/{image_name}/tags?page_size=100"
#curl -X DELETE \
#  -u "your_username:your_token" \
#  "https://hub.docker.com/v2/repositories/your_username/your_repo/tags/tag_to_delete/"


try:
    response = requests.get(docker_list_url)
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
        print(f"there are {tag_count} tags. need to delete {tag_count -5} tags")
        for i in range(5,tag_count):
            tag_to_del=tag_list[i][0]
            delete_url = f"https://hub.docker.com/v2/repositories/{username}/{image_name}/tags/{tag_to_del}/"
            print(f"Deleting tag : {tag_to_del}")
            #del_response = requests.delete(delete_url,auth=(username,docker_token))
            #if del_response.status_code == 204:
            #    print(f"✅ Successfully deleted tag: {tag_to_del}")
            #elif del_response.status_code == 404:
            #    print(f"⚠️ Tag not found: {tag_to_del}")
            #else:
            #     print(del_response.text)

    else:
        pass
except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
except KeyError as e:
        print(f"Missing expected data in response: {e}")
except Exception as e:
        print(f"An unexpected error occurred: {e}")


