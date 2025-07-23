import os
import sys
import requests


def get_dockerhub_tag_list(username,image_name):
    docker_list_url=f"https://hub.docker.com/v2/repositories/{username}/{image_name}/tags?page_size=100"

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
        output = {
            "image": f"{username}/{image_name}",
            "tag_count": tag_count,
            "total_tags" : tag_list,
            "to_delete": []
        }
        if tag_count >= 5:
            for i in range(5,tag_count):
                tag_to_del=tag_list[i][0]
               # delete_url = f"https://hub.docker.com/v2/repositories/{username}/{image_name}/tags/{tag_to_del}/"
               # print(f"Deleting tag : {tag_to_del}")
                output['to_delete'].append(tag_to_del)
        return output
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except KeyError as e:
        return {"error": f"Missing expected data in response: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


username="akhilanilkumar10"
image_name="java-web-app"

tag_out=get_dockerhub_tag_list(username,image_name) 

print(tag_out)

email_content=f"""
Hi,
Docker image : {username}/{image_name}
Tags : {tag_out['tag_count']}
"""
lines=[]
lines.append(email_content)
for tag in tag_out['total_tags']:
    lines.append(f"- {tag[0]} \t (updated: {tag[1]})")
if tag_out['to_delete']:
    lines.append(f"\n \nTags to delete : {tag_out['tag_count'] - 5}")
    for tags in tag_out['to_delete']:
        lines.append(f"- {tags}")
else:
    lines.append(f"\n \nNo tags to delete since there is only {tag_out['tag_count']} tags.")

lines.append(f"\nThanks & Regards,\nAkhil Anilkumar")
email_body = "\n".join(lines)
with open("content.txt", "w") as f:
    f.write(email_body)


#curl -X DELETE \
#  -u "your_username:your_token" \
#  "https://hub.docker.com/v2/repositories/your_username/your_repo/tags/tag_to_delete/"



