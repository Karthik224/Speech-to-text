import speech_recognition as sr #it requires an active internet connection
r=sr.Recognizer()
with sr.Microphone()as source:
    print("Listening.....")
    audio=r.listen(source)
    print("Stopped")
try:
    print("Text = "+r.recognize_google(audio))
except Exception:
    print("Couldnt recieve")
    
