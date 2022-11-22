import json
import random
import time

import requests
import reddit_browser
import reddit_api

user_info = 'users.csv'
user_progress = 'users_progress.json'

user_to_vote = 'JulieWulie80'

direction = '0'
#
# with open(user_info) as fle:
#     lines = fle.readlines()
# with open(user_progress) as ste:
#     state = json.load(ste)
#
#
# def vote(method, key, direction, token, the_state):
#     data = method(user_to_vote, after=the_state[key])
#     counter = 0
#     while 'data' in data and 'children' in data['data'] and len(data['data']['children']) > 0:
#         children = data['data']['children']
#         for child in children:
#             counter += 1
#             name = child['data']['name']
#             print(name)
#             if not child['data']['archived']:
#                reddit_api.vote(direction, name, token)
#             the_state[key] = name
#             time.sleep(random.random())
#             if counter % 25 == 0:
#                 with open(user_progress, 'w') as ste:
#                     json.dump(state, ste, indent=4)
#
#         data = method(user_to_vote, after=the_state[key])
#
#
# for line in lines:
#     try:
#         arr = line.split('|')
#         user = arr[0]
#         passwd = arr[1]
#         driver = reddit_browser.get_driver()
#         token = reddit_browser.get_token(driver, user, passwd)
#         driver.close()
#         print('about to update state')
#         if user not in state.keys():
#             state[user] = {
#                 user_to_vote: {
#                     'dir': direction,
#                     'status': 'started',
#                     'comments': None,
#                     'submitted': None
#                 }}
#         elif user_to_vote not in state[user]:
#             state[user][user_to_vote] = {
#                 'dir': direction,
#                 'status': 'started',
#                 'comments': None,
#                 'submitted': None
#             }
#         the_state = state[user][user_to_vote]
#         if the_state['status'] == 'done':
#             continue
#         print('about to pull comments')
#         vote(reddit_api.get_comments, 'comments', direction, token, the_state)
#         print('about to pull posts')
#         vote(reddit_api.get_posts, 'submitted', direction, token, the_state)
#         the_state['status'] = 'done'
#
#
#     except Exception as e:
#         with open(user_progress, 'w') as ste:
#             json.dump(state, ste, indent=4)
#         print(e)


for i in range(2):
    driver = reddit_browser.get_driver()
    print(reddit_browser.get_token(driver, 'Known-Intention28', 'Dk%Seh3KI'))
    driver.close()
