import requests
import lolData

def physical_damage(damage, enemy_armor) :
    if enemy_armor >= 0 :
        final_damage = damage / (1 + enemy_armor * 0.01)
    else :
        final_damage = damage * (2 - (1 / (1 - enemy_armor * 0.01)))
    return final_damage

def magic_damage(damage, enemy_spellblock) :
    if enemy_spellblock >= 0 :
        final_damage = damage / (1 + enemy_spellblock * 0.01)
    else :
        final_damage = damage * (2 - (1 / (1 - enemy_spellblock * 0.01)))
    return final_damage

def true_damage(damage) :
    return damage


# 파라미터는 콤보(string, QWE평 등), 상대 캐릭터 정보, 아이템 정보, 현재 캐릭터의 레벨
# 각 콤보에 대해 계산하여 물리/마법/고정 피해 따로 계산하여 최종 데미지를 나타낼 예정
def main() :
    result_damage = 0
    return result_damage