import sys

player1_mark = "P1"
player2_mark = "P2"

class TicTacToe():
    def __init__(self):
        self.state = [0,1,2,3,4,5,6,7,8]#[0]*9
        self.legal_actions = [0,1,2,3,4,5,6,7,8]
        self.turn = 0
        self.done = False
        self.reward = [0,0]
        self.winner = "winner"

    def render(self):
        print("--------")
        print("%2s %2s %2s"%(str(self.state[0]), str(self.state[1]), str(self.state[2])))
        print("%2s %2s %2s"%(str(self.state[3]), str(self.state[4]), str(self.state[5])))
        print("%2s %2s %2s"%(str(self.state[6]), str(self.state[7]), str(self.state[8])))
        print("--------")

    def step(self, action):
        if self.state[action] != player1_mark and self.state[action] != player2_mark:
           # self.state[action] = self.turn
            if self.turn == 0: self.state[action] = player1_mark
            else: self.state[action] = player2_mark
        else:
            print("ERR")
            sys.exit()
        self.legal_actions.remove(action)
        self.terminal_check()
        if self.turn == 0: self.turn=1
        else: self.turn=0
        return self.state, self.reward, self.done, self.winner

    def reset(self):
        self.state = [0,1,2,3,4,5,6,7,8]#[0]*9
        self.done = False
        self.render()
        return self.state, self.reward, self.done, self.winner

    def terminal_check(self):
        if self.state[0]==self.state[1]==self.state[2] or self.state[3]==self.state[4]==self.state[5] or self.state[6]==self.state[7]==self.state[8] or self.state[0]==self.state[3]==self.state[6] or self.state[1]==self.state[4]==self.state[7] or self.state[2]==self.state[5]==self.state[8] or self.state[0]==self.state[4]==self.state[8] or self.state[2]==self.state[4]==self.state[6]:
            self.done = True
            self.reward[self.turn] = 1
            self.reward[self.turn-1] = -1
            self.winner = self.winner_check()
        elif self.legal_actions == []: # Draw
            self.done = True
            self.reward[self.turn] = 0
        else: self.done = False

    def winner_check(self):
        return self.reward.index(1)+1