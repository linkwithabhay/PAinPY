import speech_recognition as sr
import pyttsx3
# Local Modules
from manipulate import terminal
from app import storage

class Voice_Assistant():
  '''Initialize the voice interaction between user and assistant'''
  def __init__(self):
    self.r = sr.Recognizer()
    self.engine = pyttsx3.init()
    data = storage.getItem("assistant", ["engine"])
    if not data:
      # Restart or Ask to download again
      terminal.shutDown(0)
      pass
    if "rate" in data.keys():
      self.engine.setProperty("rate", 150)
    if "voice_id" in data.keys():
      self.engine.setProperty("voice", data["voice_id"])
    self.speak("Good Morning Sensai")
    self.speak("What are we going to do today Sensai")
    while 1:
      voice = self.listen()
      if voice: self.response(voice)

  def speak(self, command: str):
    print(command)
    self.engine.say(command)
    self.engine.runAndWait()

  def listen(self, errMsg: str = ""):
    if errMsg:
      self.speak(errMsg)
    self.device_index = 1
    for index, mic in enumerate(sr.Microphone.list_microphone_names()):
      if "Headset" in mic:
        self.device_index = index
        break
    with sr.Microphone(device_index=self.device_index) as source:
      self.r.pause_threshold = 1
      self.r.adjust_for_ambient_noise(source, duration=1)
      self.r.dynamic_energy_threshold = True
      print("Listening...")
      audio = self.r.listen(source, phrase_time_limit=3)
    try:
      voice_to_text = self.r.recognize_google(audio)
      self.response(voice_to_text)
    except sr.UnknownValueError:
      return self.listen("Sorry, I did not get that. Please, say it again.")
    except sr.RequestError:
      self.speak("Sorry, my speech service is down.")
      exit(1)

  def response(self,voice: str):
    if "go to sleep" in voice:
      self.speak("Going to sleep. 🥱 ")
      exit(0)
    self.speak(voice)
    return

if __name__ == '__main__':
  Voice_Assistant()
  pass