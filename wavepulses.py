import wave

#assuming 16bit mono file
w = wave.open('360deg5min.wav', 'r')

print (w.getparams())

#input("Press Enter to continue...")

#manually analyzed
roughSignalAmplitude = 10800		#adjust this for the input signal

#tune this to ensure all pulses are detected
edgeTreshold = roughSignalAmplitude * 0.6

#initialize
sample = 0
prevSample = 0
foundFallingEdges = 0
foundRisingEdges = 0

#number of samples in file
nframes = w.getnframes()

for i in range(1, nframes):
	frame = w.readframes(1)
	sample = int.from_bytes(frame, byteorder='little', signed=True)

	changeDetected = False

	if(sample < (prevSample - edgeTreshold)):
		changeDetected = True
		foundFallingEdges = foundFallingEdges + 1
	
	if(sample > (prevSample + edgeTreshold)):
		changeDetected = True	
		foundRisingEdges = foundRisingEdges + 1

	#detect only changes that exceed the chosen treshold
	if(changeDetected):
		prevSample = sample

	print("sample=%06d, value=%06d, falling=%06d, rising=%06d, pulses=%06d, cycles=%06d" %(i, sample, foundFallingEdges, foundRisingEdges, (foundFallingEdges+foundRisingEdges), ((foundFallingEdges+foundRisingEdges)/2)))




w.close()
