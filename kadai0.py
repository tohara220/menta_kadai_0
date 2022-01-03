character_list = ["たんじろう","ぎゆう","ねずこ","むざん"]
character_list.append("ぜんいつ")

# for文で回して、キャラクター名を表示させる
for name in character_list:
    print(name)

# 関数でキャラクターの存否を判定する
def function(character_name):
    if character_name in character_list:
        print(f"{character_name}は存在します。")
    else:
        print(f"{character_name}は存在しません。")

function("ぜんいつ")