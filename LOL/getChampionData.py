import requests

'''
Data Dragon으로 부터 최신 version의 챔피언 정보 열람
차후 업데이트 예정
'''

version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
version_data = requests.get(version_url).json()
latest_version = str(version_data[0])

champion_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version + "/data/en_US/champion/Aatrox.json"

data = requests.get(champion_url).json()

# print(data)