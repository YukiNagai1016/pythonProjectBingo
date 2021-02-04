# coding: UTF-8
# 参加するプレイヤーの名前を設定するためのクラス
class Player:
    def __init__(self,name):
        self.name = name

    def player_generate(self):
        return str(self.name)
