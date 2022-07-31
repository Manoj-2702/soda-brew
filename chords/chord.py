import random
import math
from utils import *

# Octaves of Major Scale
single_octave = A[0, 2, 4, 5, 7, 9, 11]
double_octave = [
    *single_octave,
]
triple_octave = [*double_octave, *single_octave.map(lambda x: x + 24)]
five_to_five = [
    *single_octave.map(lambda x: x - 12)[4::],
    *single_octave,
    *single_octave.map(lambda x: x + 12)[:5],
]


class Chord:
    def __init__(self, degree, intervals, nextChordIdxs):
        self.degree = degree
        self.semitone_dist = single_octave[degree - 1]
        self.intervals = intervals
        self.nextChordIdxs = nextChordIdxs

    def degree(self):
        return self.degree

    def semitone_dist(self):
        return self.semitone_dist

    def intervals(self):
        return self.intervals

    def nextChordIdxs(self):
        return self.nextChordIdxs

    def nextChordIdx(self):
        factor = math.floor(random.random() * len(self.nextChordIdxs))
        return self.nextChordIdxs[factor]

    def generateVoicing(self, size: int):
        if size < 3:
            return self.intervals[:3]

        voicing = self.intervals[1:size]
        voicing.sort(reverse=bool(random.randint(0,1)))

        for i in range(len(voicing)):
            while voicing[i] < voicing[i - 1]:
                voicing[i] += 12
        voicing.insert(0, 0)
        return voicing

    def generateMode(self):
        return self.intervals.map(lambda x: x - 12 if x >= 12 else x)

    def __str__(self):
        return f"Chord(degree={self.degree}, intervals={self.intervals}, nextChordIdxs={self.nextChordIdxs})"