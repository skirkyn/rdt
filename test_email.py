import requests
import json
from bs4 import BeautifulSoup
from lxml import etree

address = None
secretKey = None
if not secretKey:
    create_email_resp = requests.get('https://temporarymail.com/ajax/?action=requestEmailAccess&value=random')
    if not create_email_resp.ok:
        print('Can\'t create email ' + create_email_resp.text)
        exit(1)

    res = json.loads(create_email_resp.text)
    address = res['address']
    secretKey = res['secretKey']
    print(address)
    print(secretKey)

email_id = None
while not email_id:
    print('Trying to read emails ... ')
    messages = requests.post(
        'https://temporarymail.com/ajax/?action=checkInbox&value={secretKey}'.format(secretKey=secretKey))
    if not messages.ok:
        print('Can\'t read email ' + messages.text)
        exit(1)

    email_list = json.loads(messages.text)
    email_id_list = list(filter(lambda k: email_list[k]['from'] == 'noreply@reddit.com', email_list.keys()))
    if len(email_id_list):
        email_id = email_id_list[0]

email_body = requests.get(
    'https://temporarymail.com/view/?i={id}&width=930'.format(id=email_id))
if not email_body.ok:
    print('Can\'t read email body ' + email_body.text)
    exit(1)


soup = BeautifulSoup(email_body.text, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('//*[text()="Verify Email Address"]/../..')[0].get('href').replace('hxxps://', 'https://'))
# {"address":"Darri.Raff@AllFreeMail.net","secretKey":"ewXMr0xmnka6iA0DTU8tNCSngGPiWEEA"}
