""" Documentation Section: """

#! Status: ONLINE
#! Version: 1.0
#! Latest Modification (Date / Month / Year): "10 / 10 / 2024"

#!</>

""" Built-In Modules Imports: """

#? SQL Connector Module:
import mysql.connector
#? Random Module:
import random

#!</>

""" Global Declaration: """

#? Project Name
projectName = "PixelTagzZ"
#? Project Utility:
projectUtility = "Valorant - Riot Games Inc."
#? Dev Name
devName = "Yashank Yadav"
#? Dev In-Game Name
devInGameName = "ChampKillzZ"
#? Dev Youtube
devGamingYoutube = "ChampKillzZ"
#? Dev Instagram:
devGamingInstagram = "champkillzz"

#!</>

""" User-Defined Functions: """

#? Connecting To Database Function:
def databaseConnectFunc():
    myDB = mysql.connector.connect(
    host = "localhost", 
    port = "3306", 
    username = "********", 
    passwd = "******", 
    database = "PixelTagzZ"
    )
    myCursor = myDB.cursor()
    return myDB, myCursor

#? Greeting Message Function:
def welcomeMsg():
    print(f"Welcome To {projectName}!!")

#? User In-Game Name Function:
def userInGameNameFunc():
    userInGameName = input(f"Kindly, enter your in-game name: ")
    return userInGameName

#? User Age Function:
def userAgeFunc():
    while True:
        try:
            userAge = int(input("Kindly, enter your age: "))
            if userAge in range(1, 101):
                break
            else:
                print("\nAge must be between 1 and 100.\n")
        except:
            print("\nInvalid input.\n")
    return userAge

#? User Country Function:
def userCountryFunc():
    userCountry = input(f"Kindly, enter your country name: ").upper()
    return userCountry

#? User Social Handles Function:
def userSocialsFunc():
    userYoutubeConfirm = userTwitchConfirm = userInstagramConfirm = ""
    while True:
        print("Do you have a YouTube channel?")
        userYoutubeConfirm = input(f"Type 'YES' (or) 'NO': ").lower()
        if userYoutubeConfirm in ['yes', 'no']:
            break
        else:
            print(f"\nInvalid input.\n")
    while True:
        print("Do you have a Twitch channel?")
        userTwitchConfirm = input(f"Type 'YES' (or) 'NO': ").lower()
        if userTwitchConfirm in ['yes', 'no']:
            break
        else:
            print(f"\nInvalid input.\n")
    while True:
        print("Do you have an Instagram account?")
        userInstagramConfirm = input(f"Type 'YES' (or) 'NO': ").lower()
        if userInstagramConfirm in ['yes', 'no']:
            break
        else:
            print(f"\nInvalid input.\n")
    return userYoutubeConfirm, userTwitchConfirm, userInstagramConfirm

#? Project Description Function:
def projectDescriptionFunc(userInGameName):
    print(f"Hello, {userInGameName}! I'm {devName}.\n"
            f"I have faced a lot of difficulties in finding optimized tags for my valorant gaming content.\n"
            f"Hence was motivated to build a tags generator for myself and the gaming community.\n"
            f"{projectName} will provide you with utmost \"Trending\" & \"Optimized\" tags!")

#? Gratitude Message Function:
def gratitudeMsg(userInGameName):
    print(f"Thank you so much for using {projectName}!\n"
            f"You can utilize these tags across various media platforms.\n" 
            f"Do not forget to,\n"
            f"MENTION: (@{devGamingYoutube}) on YouTube.\n"
            f"TAG: (#{devGamingInstagram}) on Instagram.\n"
            f"Have a great day, {userInGameName}!\n")

#? Disconnecting The Database Function:
def databaseDisconnectFunc(myDB, myCursor):
    myCursor.close()
    myDB.close()

#!</>

""" Class: """ 

#? Valorant Class:
class Valorant():
    
    #? Initialization Function:
    def __init__(self, myCursor):
        myCursor.execute("SELECT * FROM ValorantGameData;")
        valorantGameData = myCursor.fetchall()
        valorantModes = []
        valorantMaps = []
        valorantAgents = []
        valorantWeapons = []
        valorantRanks = []
        categoryLists = {
            0: valorantModes,   # Modes
            1: valorantMaps,    # Maps
            2: valorantAgents,  # Agents
            3: valorantWeapons, # Weapons
            4: valorantRanks    # Ranks
        }
        for row in valorantGameData:
            for index, item in enumerate(row):
                if item != "":
                    categoryLists[index].append(item)
        self.modes = valorantModes
        self.maps = valorantMaps
        self.agents = valorantAgents
        self.weapons = valorantWeapons
        self.ranks = valorantRanks

    #? Representation Function:
    def __str__(self):
        return (f"Valorant is a 5v5 character-based tactical first-person shooter (FPS).\n"
                f"Including '{len(self.modes)}' modes: {self.modes}.\n"
                f"With '{len(self.maps)}' different maps: {self.maps}.\n"
                f"Top level '{len(self.agents)}' agents: {self.agents}.\n"
                f"Most powerful '{len(self.weapons)}' weapons: {self.weapons}.\n"
                f"And '{len(self.ranks)}' ranks to compete: {self.ranks}.")

    #? User Game Function:
    def userGame(self):
        print(f"Kindly, describe your gaming experience.")
        while True:
            print(f"\nWhich valorant mode were you playing?")
            print(f"{self.modes}")
            userValorantMode = input (f"Kindly, enter the mode name: \n").upper()
            if userValorantMode in self.modes:
                break
            else:
                print(f"\nInvalid input.\n")
        while True:
            print(f"\nWhich valorant map were you playing on?")
            print(f"{self.maps}")
            userValorantMap = input(f"Kindly, enter the map name: \n").upper()
            if userValorantMap in self.maps:
                break
            else:
                print(f"\nInvalid input.\n")
        while True:
            print("\nWhich valorant agent were you playing with?")
            print(f"{self.agents}")
            userValorantAgent = input(f"Kindly, enter the agent name: \n").upper()
            if userValorantAgent in self.agents:
                break
            else:
                print(f"\nInvalid input.\n")
        while True:
            print("\nWhich valorant weapon were you playing with?")
            print(f"{self.weapons}")
            userValorantWeapon = input(f"Kindly, enter the weapon name: \n").upper()
            if userValorantWeapon in self.weapons:
                break
            else:
                print(f"\nInvalid input.\n")
        while True:
            print("\nWhat's your rank in valorant?")
            print(f"{self.ranks}")
            userValorantRank = input(f"Kindly, enter the rank name: \n").upper()
            if userValorantRank in self.ranks:
                break
            else:
                print(f"\nInvalid input.\n")
        return userValorantMode, userValorantMap, userValorantAgent, userValorantWeapon, userValorantRank

    #? User Gamer Tags Algorithm:
    def userGamerTagsAlgo(myCursor):
        myCursor.execute("SELECT * FROM ValorantTagsData;")
        valorantTagsData = myCursor.fetchall()
        valorantGamerTags = []
        valorantGamingTags = []
        valorantGameTags = []
        categoryLists = {
            0: valorantGamerTags,   # Gamer
            1: valorantGamingTags,  # Gaming
            2: valorantGameTags,    # Game
        }
        for row in valorantTagsData:
            for index, item in enumerate(row):
                if item != "":
                    categoryLists[index].append(item)
        userValorantGamerTags = random.sample(valorantGamerTags, k = 5)
        userValorantGamingTags = random.sample(valorantGamingTags, k = 5)
        userValorantGameTags = random.sample(valorantGameTags, k = 10)
        return userValorantGamerTags, userValorantGamingTags, userValorantGameTags

    #? User Valorant Tags Algorithm:
    def userValorantTagsAlgo(myCursor, userValorantMode, userValorantMap, userValorantAgent, userValorantWeapon, userValorantRank):
        userValorantTags = []
        valorantModeTags = []
        if userValorantMode in ["COMPETITIVE", "UNRATED", "SPIKERUSH", "DEATHMATCH", "TEAMDEATHMATCH"]:
            valorantModeTags = [f"VALORANT{userValorantMode}", f"{userValorantMode}"]
        else:
            valorantModeTags = [f"VALORANT{userValorantMode}"]
        valorantMapTags = [f"VALORANT{userValorantMap}", f"VALORANT{userValorantMap}MAPGAMEPLAY"]
        valorantAgentTags = [f"VALORANT{userValorantAgent}", f"{userValorantAgent}", f"VALORANT{userValorantAgent}GAMEPLAY"]
        valorantWeaponTags = [f"VALORANT{userValorantWeapon}", f"VALORANT{userValorantWeapon}GAMEPLAY"]
        valorantRankTags = [f"VALORANT{userValorantRank}", f"{userValorantRank}VALORANT", f"VALORANT{userValorantRank}LOBBY"]
        userValorantModeTag = random.choice(valorantModeTags)
        userValorantMapTag = random.choice(valorantMapTags)
        userValorantAgentTag = random.choice(valorantAgentTags)
        userValorantWeaponTag = random.choice(valorantWeaponTags)
        userValorantRankTag = random.choice(valorantRankTags)
        userValorantTags.extend([userValorantModeTag, userValorantMapTag, userValorantAgentTag, userValorantWeaponTag, userValorantRankTag])
        return userValorantTags

    #? User Social Tags Algorithm:
    def userSocialTagsAlgo(userYoutubeConfirm, userTwitchConfirm, userInstagramConfirm):
        userSocialTags = []
        if userYoutubeConfirm == 'yes' and userTwitchConfirm == 'yes' and userInstagramConfirm == 'yes':
            userSocialTags = ["YOUTUBEGAMING", "TWITCHGAMING", "INSTAGRAMGAMING"]
        if userYoutubeConfirm == 'yes' and userTwitchConfirm == 'no' and userInstagramConfirm == 'yes':
            userSocialTags = ["YOUTUBEGAMING", "INSTAGRAMGAMING", "CONTENTCREATOR"]
        if userYoutubeConfirm == 'yes' and userTwitchConfirm == 'yes' and userInstagramConfirm == 'no':
            userSocialTags = ["YOUTUBEGAMING", "TWITCHGAMING", "STREAMER"]
        if userYoutubeConfirm == 'no' and userTwitchConfirm == 'yes' and userInstagramConfirm == 'yes':
            userSocialTags = ["INSTAGRAMGAMING", "TWITCHGAMING", "CONTENTCREATOR"]  
        if userYoutubeConfirm == 'no' and userTwitchConfirm == 'no' and userInstagramConfirm == 'no':
            userSocialTags = ["ESPORTSPLAYER", "PROFESSIONALGAMER", "NERD"]
        return userSocialTags

    #? User Tags Algorithm:
    def userTagsAlgo(userValorantGamerTags, userValorantGamingTags, userValorantGameTags, userValorantTags, userSocialTags, userCountry, userInGameName):
        userTagsList = []
        for tag in userValorantGamerTags:
            userTagsList.append(f"#{tag}")
        for tag in userValorantGamingTags:
            userTagsList.append(f"#{tag}")
        for tag in userValorantGameTags:
            userTagsList.append(f"#{tag}")
        for tag in userValorantTags:
            userTagsList.append(f"#{tag}")
        for tag in userSocialTags:
            userTagsList.append(f"#{tag}")
        random.shuffle(userTagsList)
        userTagsString = ""
        for tag in userTagsList:
            if tag == userTagsList[-1]:
                userTagsString += (tag)
            else:
                userTagsString += (tag+" ")
        userTags = (userTagsString + f" #VALORANT{userCountry}" + f" #{userInGameName}").lower()
        print(f"\nVALORANT TAGS :-\n")
        print(userTags)

#!</>

""" Logic: """

if __name__ == '__main__':
    #? Connecting To Database:
    myDB, myCursor = databaseConnectFunc()
    #? Initialization:
    valorantGame = Valorant(myCursor)
    #? Greeting Message:
    welcomeMsg()
    print()
    #? User In-Game Name:
    userInGameName = userInGameNameFunc()
    print()
    #? User Age:
    userAge = userAgeFunc()
    print()
    #? User Country:
    userCountry = userCountryFunc()
    print()
    #? User Social Handles:
    userYoutubeConfirm, userTwitchConfirm, userInstagramConfirm = userSocialsFunc()
    print()
    #? Project Description:
    projectDescriptionFunc(userInGameName)
    print()
    #? User Game:
    userValorantMode, userValorantMap, userValorantAgent, userValorantWeapon, userValorantRank = Valorant.userGame(valorantGame)
    #? User Gamer Tags Algorithm:
    userValorantGamerTags, userValorantGamingTags, userValorantGameTags = Valorant.userGamerTagsAlgo(myCursor)
    #? User Valorant Tags Algorithm:
    userValorantTags = Valorant.userValorantTagsAlgo(myCursor, userValorantMode, userValorantMap, userValorantAgent, userValorantWeapon, userValorantRank)
    #? User Social Tags Algorithm:
    userSocialTags = Valorant.userSocialTagsAlgo(userYoutubeConfirm, userTwitchConfirm, userInstagramConfirm)
    #? User Tags Algorithm:
    Valorant.userTagsAlgo(userValorantGamerTags, userValorantGamingTags, userValorantGameTags, userValorantTags, userSocialTags, userCountry, userInGameName)
    #? Gratitude Message:
    print()
    gratitudeMsg(userInGameName)
    #? Disconnecting The Database:
    databaseDisconnectFunc(myDB, myCursor)