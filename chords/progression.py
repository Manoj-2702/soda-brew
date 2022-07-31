from utils import *
from chords.chord import Chord
from chords.chords import Chords
import math
import random


class Progression:
    def __init__(self):
        self.progression = A[...]

    def generate(self, length):
        if length < 2:
            return null

        progression = A[...]
        chord = Chords[math.floor(random.random() * len(Chords))]
        for i in range(length):
            progression.append(
                Chord(chord.degree, chord.intervals, chord.nextChordIdxs)
            )
            chord = Chords[chord.nextChordIdx()]
        self.progression = progression
        return progression

