from webexteamssdk import WebexTeamsAPI
import json
import requests

# There is an integration used on the webex teams room so the bot can respond to questions.

BotAccessToken = ''
email = 'myname@domain.com'

#--------

# use webex api to set variable for test room and assign it so it called later
baseurl = "https://api.ciscospark.com/v1/"

payload  = {}
headers = {
  'Authorization': 'Bearer ',
  'Content-Type': 'application/json'
}
url = baseurl + '/rooms'

response = requests.request("GET", url, headers=headers, data=payload)
myresponse = response.json()
BradDevNetTestRoom = myresponse['items'][0]['id']
#--------------

# create variable referencing the webexsdk api
webex_api = WebexTeamsAPI(access_token=BotAccessToken)

# create room / space called "Brad-DevNet-Test"
webex_api.rooms.create('Brad-DevNet-Test')

# add email address to room and adds the user as a moderator
webex_api.memberships.create(roomId=BradDevNetTestRoom,personEmail=email,isModerator=True)

# create message welcoming the user to the room.
webex_api.messages.create(roomId=BradDevNetTestRoom,text='Welcome to the DevNet Test Room!')