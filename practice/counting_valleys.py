# Gary is an avid hiker. He tracks his hikes meticulously, paying close
# attention to small details like topography. During his last hike he took
# exactly  steps. For every step he took, he noted if it was an uphill, , or a
# downhill,  step. Gary's hikes start and end at sea level and each step up or
# down represents a  unit change in altitude. We define the following terms:
#
# A mountain is a sequence of consecutive steps above sea level, starting with
# a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a
# step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and
# print the number of valleys he walked through.
#
# For example, if Gary's path is , he first enters a valley  units deep. Then
# he climbs out an up onto a mountain  units high. Finally, he returns to sea
# level and ends his hike.

from helpers import print_output


@print_output
def counting_valleys(n: int, s: str):
    step_map = {"D": -1, "U": 1}
    valleys = 0
    in_valley = False
    cur_pos = 0
    for step in s:
        cur_pos += step_map[step]
        if cur_pos < 0:
            in_valley = True
        if cur_pos == 0 and in_valley:
            valleys += 1
            in_valley = False
    return valleys


if __name__ == '__main__':
    counting_valleys(8, "UDDDUDUU")
