import speech_recognition as sr
import os


class AudioToText:
    audio_recognizer = None
    recordings_path = None

    def __init__(self, new_recordings_path):
        self.audio_recognizer = sr.Recognizer()
        self.recordings_path = new_recordings_path

    def convert_speech(self):
        recordings = os.listdir(self.recordings_path)
        recordings.sort(key=lambda file: os.path.getctime(os.path.join(self.recordings_path, file)), reverse=True)

        question_list = []
        for recording in recordings:
            if recording not in os.listdir(self.recordings_path):
                continue
            mp3_path = os.path.join(self.recordings_path, recording)

            with sr.AudioFile(mp3_path) as source:
                audio_data = self.audio_recognizer.record(source)  # converting audio file to audio data

                # with sr.Microphone() as source:
                #     self.audio_recognizer.adjust_for_ambient_noise(source, duration=2)
                #     audio_data = self.audio_recognizer.listen(source)

                text = self.audio_recognizer.recognize_google(audio_data, language='pl-PL')
                question_list.insert(0, text)
            os.remove(mp3_path)
        return question_list


# transcriber = AudioToText("./recordings")  # path_to_recordings
# transcriber.convert_speech()
