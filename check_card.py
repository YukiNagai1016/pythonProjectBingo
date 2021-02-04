# coding: UTF-8
import numpy as np
import pprint
import time
# ビンゴカードの中身と選ばれた言葉が一致するかどうかを調べるクラス
class Check:
    def __init__(self, cards, choose_ball, player_list):
        self.cards = cards
        self.choose_ball = choose_ball
        self.player_list = player_list

    def check_card(self):
        self.bingo_cards = []
        print('カードを確認します')
        pprint.pprint(self.cards)
        for card in self.cards:
            # お気に入りワードの配列。ここの値を変えるだけで、また別の組み合わせでビンゴゲームを楽しむことができる。
            self.favorite_words = ['沖縄', '岡山', '倉敷', '箱根', '伊豆', '江ノ島', '鎌倉', '富士Q', 'みかん', 'おにぎり', 'バドミントン', 'ラクーア', 'ディズニー','ランニング', '料理', 'カフェ', 'ドライブ', 'ウミガメ', 'モノポリー', '若者のすべて', '団子', '卵かけご飯', 'すき焼き', '秋葉原', 'ゲストハウス', '直島', '草間彌生', 'ニンニク', 'レッドブル', 'ガラスの森', '花火', '銭湯', '祐天寺', '自由が丘', '伊豆美術館', 'フォレスト', '海鮮丼', '有鄰庵', 'ルワンダ', 'ショッピング', 'バイキング', '九絵', '大岡山', 'サンドウィッチ', 'ペニー', 'ピーコックストア', 'ガーデンズ', 'タリーズ', '珈琲館', '浅草', 'メロンパン', 'ドマーレ', 'バラ', '卵焼き', 'ハーベスト', '雪合戦', 'プロジェクター', '電子カイロ', '充電器', '初代', 'かき氷', '焼き鳥', '沖縄そば', 'ジェットコースター', 'グラウンド', 'ケーキ', '金タレ', 'GOTO', 'Netflix', '浴衣', '整体','昼寝', 'マジカルバナナ', 'しりとり', 'ガイスター', '伝串']
            self.col_num = -1
            for card_num in card:
                self.col_num += 1
                for num in card_num:
                    if num == self.favorite_words[self.choose_ball]:
                        row_num = int(card_num.index(num))
                        card[self.col_num][row_num] = '*'
                        player_index = self.cards.index(card)
                        player = self.player_list[player_index]
                        print("{}さんのカードに同じ言葉がありました".format(player))
                        pprint.pprint(card)
                        check = np.array(card)
                        result1 = np.all(check == '*', axis = 0)
                        result2 = np.all(check == '*', axis = 1)
                        result3 = np.all(np.diag(check) == '*')
                        result4 = np.all(np.fliplr(check) == '*')
                        if 1 in result1 or 1 in result2:
                            result = 1
                        elif result3 == 1 or result4 == 1:
                            result = 1
                        else:
                            result = 0

                        if result == 1:
                            print('{}さんがBingoとなりました！'.format(player))
                            time.sleep(3)
                            print('--------------------------------------------------------------------')
                            pprint.pprint(card)
                            time.sleep(3)
                            print('--------------------------------------------------------------------')
                            self.bingo_cards.append(card)
                        else:
                            pass

        return self.bingo_cards
