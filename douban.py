import requests
import json

# define request url
url ="https://movie.douban.com/top250"
# deifne request header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
# wheel bulid for requst parameter and send requst
for page_start in range(0,100,20):
    params = {
        "type":"movie",
        "tag":"热门",
        "sort":"recommend",
        "page_limit":"20",
        "page_start":page_start
    }
    reponse = requests.get(
        url = url,
        headers = headers,
        params = params,
    )
    results = reponse.json()
    print(results)
    print("finished!")