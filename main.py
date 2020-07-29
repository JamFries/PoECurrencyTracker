import requests
import json
import time

# Set initial variables used when searching through APIs
league = 'Harvest'
account = 'JamFries'
platform = 'pc'
charName = 'NowCalledAuraStacking'

playerStashTab = []
playerTabChangeID = 'no'

changeID = '776710358-789939671-754199643-853094474-813985060'
# Follow the river until my account's first stash is found
while playerTabChangeID == 'no':
    stashTabs = requests.get('http://api.pathofexile.com/public-stash-tabs', dict(id=changeID)).json()
    nextChangeID = stashTabs['next_change_id']

    #Check to see if there is no content (head of the river?)
    if len(stashTabs['stashes']) < 1:
        print("No content...Sleeping for 2 seconds")
        time.sleep(2)

    # Search each tab to check if I am the owner
    for entry in stashTabs['stashes']:
        if (entry['accountName'] == account):
            print(entry['id'])
            playerTabChangeID = changeID # A tab of my account was found and the changeID was recorded for future reference
            print(playerTabChangeID)
            break
    changeID = nextChangeID # Otherwise move to the next set of stash tabs
    print("done, sleeping for 1 second")
    time.sleep(1)



##############################################
# # Gather a list of all public stash tabs that belong to the player's account
# playerStashTabs = []
#
# # Use pathofexile's stash tab API to find my stash tabs that are listed public
# # Start with the change id from poe.ninja
# changeID = '776469591-789811728-754081559-852962907-813854915'
# stashTabs = requests.get('http://api.pathofexile.com/public-stash-tabs', dict(id=changeID)).json()
# nextChangeID = stashTabs['next_change_id']
#
#
# # Check each stash from the api for the specific account
# for entry in stashTabs['stashes']:
#     if (entry['accountName'] == account):
#         playerStashTabs.append(entry) #Add the stash entry to the list of stash tabs the account has
#
# print(playerStashTabs)
# #changeID = nextChangeID
#
