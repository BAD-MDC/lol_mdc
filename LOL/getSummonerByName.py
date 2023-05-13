import requests
from urllib import parse
import mdcAPI

'''
입력값 : 소환사명
불러오는 정보 : id, accountId, puuid 등
함수명 : getId, getAccountId, getPuuid, getSummoner
*** requests module error 발생 시 pip install requests 진행할 것. ***
'''
APIKey = mdcAPI.API

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": APIKey
}

# ID 값 받아오기
def getId(summonerName) :
    encodingSummonerName = parse.quote(summonerName)
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(URL, headers=headers)
    data = res.json()
    return data["id"]

# AccountID 값 받아오기
def getAccountId(summonerName) :
    encodingSummonerName = parse.quote(summonerName)
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(URL, headers=headers)
    data = res.json()
    return data["accountId"]

# PUUID 값 받아오기
def getPuuid(summonerName) :
    encodingSummonerName = parse.quote(summonerName)
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(URL, headers=headers)
    data = res.json()
    return data["puuid"]

# Summoner 전체 정보 열람
def getSummoner(summonerName) :
    encodingSummonerName = parse.quote(summonerName)
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(URL, headers=headers)
    data = res.json()
    return data
