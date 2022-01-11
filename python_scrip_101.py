import argparse #สำหรับ รับ input จากภายนอก 
import subprocess #สำหรับ run terminal command

#import flask #สำหรับ ทำ web app และ web service api


def print_other():
    print('something else')

def parse_input():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument(
        'M',
        type=int,
        help='value of M Positional argument')

    parser.add_argument(
        '--x',
        type=int,
        help='value of x')

    parser.add_argument(
        '--yval',
        type=int,
        default=3,
        help='value of y')
    args = parser.parse_args()
    return args

if __name__ == "__main__":

    args = parse_input()

    x = args.x
    y = args.yval
    print(f'M = {args.M}')
    print(f'calculate {x} x {y} = {x*y}')


