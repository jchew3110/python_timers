#Use like this: python accurate_complicated_timer.py -h 1 -m 30 20
#(sets a timer for 1 hour 30 minutes and 20 seconds)

import time
import datetime
import argparse


def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_second_later = datetime.timedelta(seconds=1)
    for remaining in range(x, 0, -1):
        target += one_second_later
        print(datetime.timedelta(seconds=remaining), 'remaining', end='\r')
        time.sleep((target - now()).total_seconds())
    print('\nTIMER ended')


def command_line_parser():
    parser = argparse.ArgumentParser(description='Simple countdown timer', conflict_handler='resolve')
    parser.add_argument('seconds', type=int, help='amount of seconds to wait for')
    parser.add_argument('-m', '--minutes', '--min', type=int, help='additional amount of minutes to wait for')
    parser.add_argument('-h', '--hours', type=int, help='additional amount of hours to wait for')
    return parser


if __name__ == '__main__':
    args = command_line_parser().parse_args()
    delay = datetime.timedelta(**vars(args))
    print('Starting countdown for', delay)
    countdown_timer(int(delay.total_seconds()))
