# coding: UTF-8
import numpy as np
import random
import pprint

# ビンゴカード作成のためのクラス
class BingoCard:
    
    def generate_card(self):
        self.numbers = []
        self.card_numbers = []
        self.detail_bingo_card_numbers = []
        self.bingo_card_numbers = []
        self.upper = 16
        self.under = 1
        self.count = 0

        while len(self.card_numbers) < 5:
            # お気に入りワードの配列。ここの値を変えるだけで、また別の組み合わせでビンゴゲームを楽しむことができる。
            self.favorite_words = ['沖縄', '岡山', '倉敷', '箱根', '伊豆', '江ノ島', '鎌倉', '富士Q', 'みかん', 'おにぎり', 'バドミントン', 'ラクーア', 'ディズニー','ランニング', '料理', 'カフェ', 'ドライブ', 'ウミガメ', 'モノポリー', '若者のすべて', '団子', '卵かけご飯', 'すき焼き', '秋葉原', 'ゲストハウス', '直島', '草間彌生', 'ニンニク', 'レッドブル', 'ガラスの森', '花火', '銭湯', '祐天寺', '自由が丘', '伊豆美術館', 'フォレスト', '海鮮丼', '有鄰庵', 'ルワンダ', 'ショッピング', 'バイキング', '九絵', '大岡山', 'サンドウィッチ', 'ペニー', 'ピーコックストア', 'ガーデンズ', 'タリーズ', '珈琲館', '浅草', 'メロンパン', 'ドマーレ', 'バラ', '卵焼き', 'ハーベスト', '雪合戦', 'プロジェクター', '電子カイロ', '充電器', '初代', 'かき氷', '焼き鳥', '沖縄そば', 'ジェットコースター', 'グラウンド', 'ケーキ', '金タレ', 'GOTO', 'Netflix', '浴衣', '整体','昼寝', 'マジカルバナナ', 'しりとり', 'ガイスター', '伝串']
            [self.numbers.append(number) for number in range(self.under, self.upper)]
            self.card_numbers.append(np.random.choice(self.numbers, 5, replace = False))
            
            for i in range(5):
                self.detail_bingo_card_numbers.append(self.favorite_words[self.card_numbers[self.count][i]])
        
            self.bingo_card_numbers.append(self.detail_bingo_card_numbers)
            self.upper += 15
            self.under += 15
            self.count += 1
            self.numbers = []
            self.detail_bingo_card_numbers = []
        else:
            self.card = np.array(self.bingo_card_numbers).T.tolist()
            self.card[2][2] = '*'
            return self.card
