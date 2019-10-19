from gtts import gTTS

tts = gTTS(text="今天好生氣喔！", lang="zh-tw")
tts.save("happy.ogg")