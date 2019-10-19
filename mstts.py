import sapi

def get_name():
    voice = sapi.Sapi()
    voices = voice.voice.GetVoices()
    for v in voices:
        print(v.GetDescription())

def create(name="Hanhan", filename="output.wav", message="測試", rate=0, volume=50):
    voice = sapi.Sapi()
    voice.set_voice(name)
    voice.set_rate(rate)
    voice.voice.Volume = volume
    voice.create_recording(filename, message)
    voice.say(message)