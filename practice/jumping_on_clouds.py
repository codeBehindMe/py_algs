# Emma is playing a new mobile game that starts with consecutively numbered
# clouds. Some of the clouds are thunderheads and others are cumulus. She can
# jump on any cumulus cloud having a number that is equal to the number of the
# current cloud plus  or . She must avoid the thunderheads. Determine the
# minimum number of jumps it will take Emma to jump from her starting postion
# to the last cloud. It is always possible to win the game.
#
# For each game, Emma will get an array of clouds numbered  if they are safe
# or  if they must be avoided. For example,  indexed from . The number on each
# cloud is its index in the list so she must avoid the clouds at indexes  and
# . She could follow the following two paths:  or . The first path takes jumps
# while the second takes .

# FIXME: Description
from helpers import print_output


@print_output
def jumping_on_clouds(c: [int]):
    steps = 0
    cur_pos = 0  # Current position.
    finished = False
    while not finished:
        try:
            if c[cur_pos + 2] != 1:
                steps += 1
                cur_pos += 2
            else:
                steps += 1
                cur_pos += 1
        except IndexError:
            finished = True
    if cur_pos < len(c) - 1:
        steps += 1
    return steps


if __name__ == '__main__':
    jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
    jumping_on_clouds([0, 0, 1, 0, 0, 0, 1])
