import requests
import json

'''
Data Dragon으로 부터 최신 version의 챔피언 정보 열람
차후 업데이트 예정
'''

#Return : 가장 최신 버전 (str)
def latest_version() : 
     version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
     version_data = requests.get(version_url).json()
     latest_version = str(version_data[0])
     return latest_version

#Return : 모든 챔피언 관련 json file
def champions() :
     champions_data_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/ko_KR/champion.json"
     champions_data = requests.get(champions_data_url).json()
     return champions_data

#파라미터 : 챔피언 한국 이름
#Return : 특정 챔피언 관련 json file
def champion(champion_kor_name) :
     champion_name = champion_eng_name(champion_kor_name)
     champion_data_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/ko_KR/champion/" + champion_name + ".json"
     champion_data = requests.get(champion_data_url).json()
     return champion_data

#파라미터 : 챔피언 한국 이름 , 레벨
#Return : [ HP, MP, ARMOR, SPELLBLOCK , ATTACKDMG, ATTACKSPEED ] <- 입력된 레벨에 해당하는 값 Return
def champion_by_level(champion_kor_name, level) :
     champion_name = champion_eng_name(champion_kor_name)
     champion_info = champion(champion_kor_name)
     hp = champion_info["data"][champion_name]["stats"]["hp"]
     hpperlevel = champion_info["data"][champion_name]["stats"]["hpperlevel"]
     mp = champion_info["data"][champion_name]["stats"]["mp"]
     mpperlevel = champion_info["data"][champion_name]["stats"]["mpperlevel"]
     armor = champion_info["data"][champion_name]["stats"]["armor"]
     armorperlevel = champion_info["data"][champion_name]["stats"]["armorperlevel"]
     spellblock = champion_info["data"][champion_name]["stats"]["spellblock"]
     spellblockperlevel = champion_info["data"][champion_name]["stats"]["spellblockperlevel"]
     attackdamage = champion_info["data"][champion_name]["stats"]["attackdamage"]
     attackdamageperlevel = champion_info["data"][champion_name]["stats"]["attackdamageperlevel"]
     attackspeed = champion_info["data"][champion_name]["stats"]["attackspeed"]
     attackspeedperlevel = champion_info["data"][champion_name]["stats"]["attackspeedperlevel"]

     return [hp + hpperlevel * (level - 1), mp + mpperlevel * (level - 1), 
             armor + armorperlevel * (level - 1), spellblock + spellblockperlevel * (level - 1),
             attackdamage + attackdamageperlevel * (level - 1), attackspeed * (1 + 0.01 * attackspeedperlevel * (level - 1))]

#파라미터 : 챔피언 한국 이름
#Return : 챔피언 영어 이름(str) , 한국 이름이 잘못된 경우 "ERROR"
def champion_eng_name(champion_kor_name) :
     for champion in champions()["data"] :
          if champions()["data"][champion]["name"] == champion_kor_name :
               return(champions()["data"][champion]["id"])
     return "ERROR"

#Return : 아이템 리스트
def items() :
     items_data_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/ko_KR/item.json"
     items_data = requests.get(items_data_url).json()
     return items_data