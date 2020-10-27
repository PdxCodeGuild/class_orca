'''The purpose of this project is to record a signal, using a micrphone or USB input
and then manipulate that sound, using pre-packaged sound effects, and then 
playing back the altered sound. '''

import pyaudio
import wave
from pysndfx import AudioEffectsChain
import wavio
import librosa
import numpy

fx = (
    AudioEffectsChain()
    .reverb()
    .phaser()
    .delay()
    .overdrive()
    )

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


infile = 'output.wav'
outfile = 'output.wav'

effect = int(input('''What effect would you like to apply?:
(1)phaser (2)delay (3)reverb (4)overdrive\n'''))
while effect not in [1,2,3,4]:
    effect = int(input("Choose 1,2,3 or 4\n"))
if effect == 1:
    fx.phaser(infile, outfile)
elif effect == 2:
    fx.delay(infile, outfile)
elif effect == 3:
    fx.reverb(infile, outfile)
elif effect == 4:
    fx.overdrive(infile, outfile)



filename = "output.wav"
# Open the sound file 
wf = wave.open(filename, 'rb')

# fx.phaser(wf)

p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(CHUNK)

# Play the sound by writing the audio data to the stream
# while data != '':
#    stream.write(data)
#    data = wf.readframes(CHUNK)

while True:
    data = wf.readframes(CHUNK)
    if not data:
        break
    stream.write(data)
#    if data == b'':
#         break

# Close and terminate the stream
stream.close()
p.terminate()
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
# wf.setchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
wf.close()

# y, sr = librosa.load("output.wav")

# y, sr = librosa.load("output.wav", sr=None)
# y = fx.phaser(y)
# # sound = wavio.read("output.wav")

# # sound = fx.phaser(sound)

# wavio.write("output.wav", y, RATE, sampwidth=2)

# wf = wave.open('output.wav', 'wb')

# wf = wave.open('output.wav', 'wb')
# apply_effect ()
# infile = 'output.wav'
# outfile = 'output.wav'

# fx.phaser(infile,outfile)

# chunk = 1024  