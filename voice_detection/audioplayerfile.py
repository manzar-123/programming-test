from audioplayer import AudioPlayer

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
AudioPlayer("C:/Users/Manzar/OneDrive - Aga Khan University/R/programming/yesSir.mp3").play(block=True)