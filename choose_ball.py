# coding: UTF-8
import random

# ビンゴの数字を一つ選ぶためのクラス
class ChoiceMachine:
    def __init__(self):
        self.balls = [number for number in range(1,76)]
        self.choose_balls = []

    def choose_ball(self):
        self.ball = random.choice(self.balls)
        self.balls.remove(self.ball)
        self.choose_balls.append(self.ball)
        return self.ball
