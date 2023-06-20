# [LoL_MDC][lolmdclink]
[lolmdclink]: https://bad-mdc.github.io/lol_mdc/
위 링크를 통해 LOL_MDC 로 접속할 수 있습니다.

[![pages-build-deployment](https://github.com/BAD-MDC/lol_mdc/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/BAD-MDC/lol_mdc/actions/workflows/pages/pages-build-deployment)


## GOAL

Riot Games API를 이용하여 League of Legends 관련 데이터를 수집하고, 챔피언 데미지 시뮬레이터, 챔피언 별 승률 및 시너지를 고려하여 기대 승률 및 초/중/후반 우세도, 특정 챔피언과 시너지를 내는 챔피언 등을 알려주는 웹사이트를 개발

## DETAILS

### Special Thanks to : [lolstaticdata](https://github.com/meraki-analytics/lolstaticdata)

1. 특정 콤보에 대한 실제 데미지 ( 방어력, 마법 저항력, 스킬 계수 등 종합적 고려 ) 계산 시뮬레이터
2. 5v5 상황에서, 각 챔피언들의 데이터를 통해 5개의 챔피언 조합 시 기대 승률, 및 상대 팀의 챔피언과의 상대 승률 등을 조합하여 각 팀의 기대 승률 제공
(플레이어의 챔피언 숙련도 및 챔피언 승률 등도 고려할 예정)
3. 특정 챔피언에 대하여, 상대로 마주했을 때 상대하기 어려운 챔피언 및 쉬운 챔피언 제공 
라인별로 같은 라인일 때의 데이터 제공.
4. 특정 챔피언에 대하여 아군으로 만났을 때 시너지를 낼 수 있는(기대 승률이 올라가는) 챔피언 목록 제공. 반대로 시너지가 나오지 않는 아군 리스트 제공.
