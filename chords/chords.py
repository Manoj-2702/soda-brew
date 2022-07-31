from utils import *
from chords.chord import Chord

toChordIdxs = lambda arr: arr.map(lambda n: n - 1)

I = Chord(1, A[0, 4, 7, 11, 14, 17, 21], toChordIdxs(A[2, 3, 4, 5, 6, 7]))
ii = Chord(2, A[0, 3, 7, 10, 13, 17, 20], toChordIdxs(A[3, 5, 7]))
iii = Chord(3, A[0, 3, 7, 10, 13, 17, 20], toChordIdxs(A[4, 6]))
IV = Chord(4, A[0, 4, 7, 11, 14, 18, 21], toChordIdxs(A[2, 5]))
V = Chord(5, A[0, 4, 7, 10, 14, 17, 21], toChordIdxs(A[1, 3, 6]))
vi = Chord(6, A[0, 3, 7, 10, 14, 17, 20], toChordIdxs(A[2, 4]))
vii = Chord(7, A[0, 3, 6, 10, 13, 17, 20], toChordIdxs(A[1, 3]))

Chords = [I, ii, iii, IV, V, vi, vii]
