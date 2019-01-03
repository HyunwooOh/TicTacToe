import argparse
import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--p1", default='random', type = str, help="human, random")
    parser.add_argument("--p2", default='random', type = str, help="human, random")

    ##############################################
    args = parser.parse_args()
    ##############################################
    run.play(args)

if __name__ == "__main__":
    main()