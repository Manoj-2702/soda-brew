from chords.progression import Progression
from midiutil import MIDIFile
from music21 import *
from utils import *
import random

track = 0
time = 0
myMidi = MIDIFile(5)
myMidi.addTrackName(track, time, "Chords")
myMidi.addTempo(track, time, 100)

channel = 0
duration = 4
volume = 100

# generate a random progression
progression = Progression().generate(5)

for i in progression:
    root=note.Note("C3").transpose(i.semitone_dist)  
    voicings = i.generateVoicing(4)
    c = chord.Chord(voicings)
    for i in c.pitches:
        myMidi.addNote(track, channel, root.pitch.midi + i.midi, time, duration, volume)
    time += duration


with open("testOutput.mid", "wb") as f:
    myMidi.writeFile(f)
