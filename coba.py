import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    location = []
    tempScore = scores
    locIndex = 0
    for i in alice:
        tempScore.append(i)
        numOfRank = list(set(tempScore))
        numOfRank.sort(reverse = True)
        locIndex = numOfRank.index(i)+1
        location.append(locIndex)
        tempScore = tempScore[:locIndex]
    return location

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()