import requests
import json

# Set initial variables used when searching through APIs
league = 'Harvest'
account = 'jamfries'
platform = 'pc'

# Gather a list of all public stash tabs that belong to the player's account
playerStashTabs = []

# Use pathofexile's stash tab API to find my stash tabs that are listed public
# Start with the change id from poe.ninja
changeID = '776469591-789811728-754081559-852962907-813854915'
stashTabs = requests.get('http://api.pathofexile.com/public-stash-tabs', dict(id=changeID)).json()
nextChangeID = stashTabs['next_change_id']
#print(nextChangeID)
#print(stashTabs)

# Check each stash from the api for the specific account
for entry in stashTabs['stashes']:
    if (entry['accountName'] == 'Hinash'):
        playerStashTabs.append(entry) #Add the stash entry to the list of stash tabs the account has
#print(playerStashTabs)









getCurrencyValues = requests.get('https://poe.ninja/api/data/currencyoverview?league=' + league + '&type=Currency').json()

# Use pathofexile's api to get a single character's equipped items
charName = 'NowCalledAuraStacking'
getAccount = requests.get('https://pathofexile.com/character-window/get-items', dict(character=charName, accountName=account)).json()