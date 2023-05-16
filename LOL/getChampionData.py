import requests

'''
Data Dragon으로 부터 최신 version의 챔피언 정보 열람
차후 업데이트 예정
'''

#모든 버전들 목록 URL
version_url = "https://ddragon.leagueoflegends.com/api/versions.json"

#가장 최신 버전 불러오기 ( 추후에 코드 수정 필요 )
version_data = requests.get(version_url).json()
latest_version = str(version_data[0])

#최신 버전의 챔피언 정보를 가지고 있는 json 파일 URL
champion_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version + "/data/en_US/champion/Aatrox.json"

data = requests.get(champion_url).json()

# print(data)