from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers.instrument import Instrument, Piano, Guitar
from mingus.containers import Composition
from mingus.midi.midi_file_out import write_Composition

eb = Note("Eb", 4)
g  = Note("G", 4)
bb  = Note("Bb", 4)
n = NoteContainer([eb, g, bb])
c = Composition()
c.set_author('Dusty Carver', 'dustycarver@gmail.com')
c.set_title('Late Nights')
t = Track(Guitar())
b = Bar('Eb', (4,4))
b.place_notes(n, 4)
b.place_notes(n, 4)
b.place_notes(n, 4)
b.place_notes(None, 4)
t.add_bar(b)
c.add_track(t)

write_Composition("one.mid", c)
