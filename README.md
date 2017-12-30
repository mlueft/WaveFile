# WaveFile
A Python class to write wave files.

```python
from WaveFile import WaveFile

samplingRate = 22000
bitRate      = 8
channels     = 1

data         = [ 255,128,100,50,0,1,128,255,...]

file = WaveFile.WaveFile(samplingRate,bitRate,channels)
file.save( "sound.wav", data )

```