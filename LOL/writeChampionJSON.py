import requests
import json
from lolData import champions

#LOL 폴더에 챔피언 정보 JSON 파일 생성
def writeChampionJSON() :

    with open('LOL/champion.json', 'w') as convert_file:
        json.dump(champions(), convert_file, ensure_ascii = False)


writeChampionJSON()