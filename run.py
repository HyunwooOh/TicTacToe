from agents.human import Human_Agent
from agents.random import Random_Agent

from env import TicTacToe
import sys

def play(args):
    env = TicTacToe()
    player1, player2 = Random_Agent(), Random_Agent()
    if args.p1 == "human": player1 = Human_Agent()
    elif args.p1 == "random": player1 = Random_Agent()
    if args.p2 == "human": player2 = Human_Agent()
    elif args.p2 == "random": player2 = Random_Agent()
    turn = 0
    sess = 1
    while True:
        done = False
        state, _, _, _ = env.reset()
        while not done:
            if turn%2 == 0:
                print("Player 1 turn")
                action = player1.choose_action(sess, state)
            else:
                print("Player 2 turn")
                action = player2.choose_action(sess, state)
            state, reward, done, info = env.step(int(action))
            env.render()
            turn+=1
        if type(info) == str: print("Draw!")
        else: print("Player %d win!"%(info))
        print("reward:", reward)
        sys.exit()