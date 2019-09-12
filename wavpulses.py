import wave
import numpy as np

w = wave.open('360deg5min.wav', 'r')


print (w.getnchannels())
print (w.getsampwidth())
print (w.getframerate())
nframes = w.getnframes()
print (nframes)
print (w.getcomptype())
print (w.getcompname())
print (w.getparams())
print (w.getcomptype())


input("Press Enter to continue...")

#manually analyzed
roughSignalAmplitude = 10800

edgeTreshold = roughSignalAmplitude * 0.6

sample = 0
prevSample = 0
prevSign = 0

foundFallingEdges = 0
foundRisingEdges = 0

for i in range(1, nframes):
	frame = w.readframes(1)
	sample = int.from_bytes(frame, byteorder='little', signed=True)

	sign = np.sign(sample)

	changeDetected = False

	if(sample < (prevSample - edgeTreshold)):
		changeDetected = True
		foundFallingEdges = foundFallingEdges + 1
	
	if(sample > (prevSample + edgeTreshold)):
		changeDetected = True	
		foundRisingEdges = foundRisingEdges + 1

	if(changeDetected):
		prevSample = sample
		prevSign = sign

	print("sampleNo=%06d, sampleData=%06d, foundFallingEdges=%06d, foundRisingEdges=%06d" %(i, sample, foundFallingEdges, foundRisingEdges))

w.close()
