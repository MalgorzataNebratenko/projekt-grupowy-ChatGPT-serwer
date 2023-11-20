import pyttsx3


class TextToAudio:
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()
        self.speaking_rate(135)
        self.volume_level(1.0)  # volume level between 0 and 1
        # self.voice_gender(0)  # 0 is male, 1 female; they are the same anyway (maybe bug?)

    def speaking_rate(self, newSpeakingRate):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', newSpeakingRate)
        return rate, newSpeakingRate

    # def volume_level(self, newVolume):
    #     volume = self.engine.getProperty('volume')
    #     self.engine.setProperty('volume', newVolume)
    #     return volume, newVolume

    # def voice_gender(self, voiceIndex):
    #     voice = self.engine.getProperty('voices')
    #     self.engine.setProperty('voices', voice[voiceIndex].id)

    def speak_to_me(self, newText):
        self.engine.say(newText)
        self.engine.runAndWait()

    def save_voice(self, newText, conversationName):
        self.engine.save_to_file(newText, f'{conversationName}.mp3')
        self.engine.runAndWait()
        return f'Saved file {conversationName} to mp3'


# speak = TextToAudio()
# speak.speak_to_me("Speak to me something")
