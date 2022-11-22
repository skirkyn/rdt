import json
import random

import requests
import ratelimit
from ratelimit import sleep_and_retry


# @sleep_and_retry
# @ratelimit.limits(calls=80, period=60)
def vote(dir, what_to_downvote, access_token,
         user_agent=f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10, 16)}_0) AppleWebKit/521.36 (KHTML, like Gecko) Chrome/{random.randint(103, 108)}.1.0.0 Safari/537.36"):
    headers = {
        'authority': 'oauth.reddit.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {access_token}',
        'cache-control': 'no-cache',
        'origin': 'https://www.reddit.com',
        'pragma': 'no-cache',
        'referer': 'https://www.reddit.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user_agent,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'id': what_to_downvote,
        'dir': dir,
        'api_type': 'json'
    }
    res = requests.post(
        'https://oauth.reddit.com/api/vote?redditWebClient=desktop2x&app=desktop2x-client-production&raw_json=1&gilding_detail=1',
        data=payload, headers=headers)

    if not res.ok:
        print(res.text)
        raise ValueError(res.text)


def get_comments(user, after=None,
                 user_agent=f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10, 16)}_0) AppleWebKit/521.36 (KHTML, like Gecko) Chrome/{random.randint(103, 108)}.1.0.0 Safari/537.36"):
    headers = {
        'authority': 'www.reddit.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agent,
    }

    res = requests.get(f'https://www.reddit.com/user/{user}/comments.json?after={after}', headers=headers)

    if not res.ok:
        print(res.text)
        raise ValueError(res.text)

    return json.loads(res.text)


def get_posts(user, after=None,
              user_agent=f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10, 16)}_0) AppleWebKit/521.36 (KHTML, like Gecko) Chrome/{random.randint(103, 108)}.1.0.0 Safari/537.36"):
    headers = {
        'authority': 'www.reddit.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agent,
    }

    res = requests.get(f'https://www.reddit.com/user/{user}/submitted.json?after={after}',
                       headers=headers)

    if not res.ok:
        print(res.text)
        raise ValueError(res.text)

    return json.loads(res.text)
