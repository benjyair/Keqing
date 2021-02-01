import json
import requests


def get_req(url, params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    html = requests.get(url=url, params=params, headers=headers).content.decode()
    # print(html)
    result = json.loads(html)
    if result["code"] == 200:
        return result["data"]
    else:
        return None
