import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def text_to_speech(Text):
    engine.say(Text)
    engine.runAndWait()

text_to_speech("hello")
