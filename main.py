import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone()as source:
	print("Speak : ")
	audio=r.listen(source)
	try:
		output=r.recognize_google(audio)
		print("You:{}".format(output))	
		if (output=="hello"):
			print("Hello to you too")
		
		if(output=="hi"):
			print("Hey, how are you?")
		

	except:
		print("I can't recognize what you said!")
