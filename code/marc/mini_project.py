from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

infile = 'output.wav'
outfile = 'processed_output_file.wav'

# Apply phaser and reverb directly to an audio file.
fx(infile)

# Or, apply the effects directly to a ndarray.
# from librosa import load
# y, sr = load(infile, sr=None)
# y = fx(y)

# Apply the effects and return the results as a ndarray.
# y = fx(infile)

# Apply the effects to a ndarray but store the resulting audio to disk.
fx(x, outfile)