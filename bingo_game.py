# coding: UTF-8
import player
from bingo_card import BingoCard
from choose_ball import ChoiceMachine
from check_card import Check
import pprint
import time
# 参加人数を決める
player_num = int(input('何人で遊ぶ？ -- 1～：　'))
player_count = 0
players = []
# お気に入りワードの配列。ここの値を変えるだけで、また別の組み合わせでビンゴゲームを楽しむことができる。
favorite_words = ['沖縄', '岡山', '倉敷', '箱根', '伊豆', '江ノ島', '鎌倉', '富士Q', 'みかん', 'おにぎり', 'バドミントン', 'ラクーア', 'ディズニー','ランニング', '料理', 'カフェ', 'ドライブ', 'ウミガメ', 'モノポリー', '若者のすべて', '団子', '卵かけご飯', 'すき焼き', '秋葉原', 'ゲストハウス', '直島', '草間彌生', 'ニンニク', 'レッドブル', 'ガラスの森', '花火', '銭湯', '祐天寺', '自由が丘', '伊豆美術館', 'フォレスト', '海鮮丼', '有鄰庵', 'ルワンダ', 'ショッピング', 'バイキング', '九絵', '大岡山', 'サンドウィッチ', 'ペニー', 'ピーコックストア', 'ガーデンズ', 'タリーズ', '珈琲館', '浅草', 'メロンパン', 'ドマーレ', 'バラ', '卵焼き', 'ハーベスト', '雪合戦', 'プロジェクター', '電子カイロ', '充電器', '初代', 'かき氷', '焼き鳥', '沖縄そば', 'ジェットコースター', 'グラウンド', 'ケーキ', '金タレ', 'GOTO', 'Netflix', '浴衣', '整体','昼寝', 'マジカルバナナ', 'しりとり', 'ガイスター', '伝串']
# 参加が揃ったら開始する
while player_count < player_num:
    player_name = input('名前を入力ください：　')
    player_ = player.Player(player_name)
    players.append(player_name)
    player_count += 1
else:
    for a in players:
        print('{}人目のプレイヤーは、{}さん'.format(players.index(a),a))
# 参加人数とカードの枚数は同じ
num_of_cards = player_num
cards = []
# プレイヤーごとにカードを作って表示させる
while num_of_cards > 0:
    card_ins = BingoCard()
    card = card_ins.generate_card()
    cards.append(card)
    num_of_cards -= 1
else:
    for player, card in zip(players, cards):
        print('{}さんのカード'.format(player))
        pprint.pprint(card)
# ビンゴカード作成のためのクラスからインスタンスを作成
machine = ChoiceMachine()
# ビンゴの数字を引く
choice_counter = 1
while len(cards) > 0:
    ball = machine.choose_ball()
    time.sleep(3)
    print('{}回目・・・引いた言葉は「{}」です'.format(choice_counter, favorite_words[ball]))
    time.sleep(3)
    check = Check(cards, ball, players)
    bingo = check.check_card()
    for bingo_card in bingo:
        player_index = cards.index(bingo_card)
        cards.remove(bingo_card)
        print('{}さんがBingoとなり、残りのカードは{}枚'.format(players[player_index],len(cards)))
        players.remove(players[player_index])
    choice_counter += 1
