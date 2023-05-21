import requests
import json
from lolData import champions
from lolData import champion
from lolData import champion_eng_name

#LOL 폴더에 전체 챔피언 정보 JSON 파일 생성
def writeChampionsJSON() :

    with open('LOL/champion_data/champion.json', 'w') as convert_file:
        json.dump(champions(), convert_file, ensure_ascii = False)

#LOL 폴더에 특정 챔피언 정보 JSON 파일 생성
def writeChampionJSON(champion_kor_name) :
    champion_name = champion_eng_name(champion_kor_name)
    champion_json_file_name = 'LOL/champion_data/' +  champion_name + '.json'
    with open(champion_json_file_name, 'w') as convert_file:
        json.dump(champion(champion_name), convert_file, ensure_ascii = False)

writeChampionsJSON()
#writeChampionJSON("루시안")