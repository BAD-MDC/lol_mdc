import requests
import json

'''
Data Dragon으로 부터 최신 version의 챔피언 정보 열람
차후 업데이트 예정
'''

#가장 최신 버전 정보 반환
def latest_version() : 
     version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
     version_data = requests.get(version_url).json()
     latest_version = str(version_data[0])
     return latest_version

#챔피언 JSON 파일 반환
def champions() :
     champion_data_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/ko_KR/champion.json"
     champion_data = requests.get(champion_data_url).json()
     return champion_data


#챔피언 이름에 따른 결과값 반환

#챔피언 레벨 입력값에 따라 정보 반환

#챔피언 목록 반환
def champion_name(champion_kor_name) :
     for champion in champions()["data"] :
          if champions()["data"][champion]["name"] == champion_kor_name :
               return(champions()["data"][champion])
     return "ERROR"     