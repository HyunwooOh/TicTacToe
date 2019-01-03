import random
from utils import check_legal_actions

class Random_Agent():
    def __init__(self):
        self.action = 0
    def choose_action(self, sess, state):
        legal_actions = check_legal_actions(state)
        self.action = random.choice(legal_actions)
        return self.action
