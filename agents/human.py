import random
from utils import check_legal_actions

class Human_Agent():
    def __init__(self):
        self.action = 0
    def choose_action(self, sess, state):
        self.action = input("action:")
        return self.action
