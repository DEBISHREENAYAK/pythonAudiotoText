import speech_recognition as sr

l = sr.Recognizer()

with sr.Microphone() as source:
    print('listening ..: ')
    audio =l.listen(source)
try:
     text = l.recognize_google(audio)
     #print('you said : {}'.format(text))
     print(format(text))

except:
     print('sorry could not recognize your voice')


