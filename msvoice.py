import mstts
import soundfile as sf

filename = "Dino"
text = "Dino，你好可愛！"
mstts.create(name="Hanhan", 
             filename=filename+".wav",
             message=text, 
             rate=0, 
             volume=100)

# 使用 PySoundFile 把 .wav 檔，轉成 .ogg 檔
data, samplerate = sf.read(filename+".wav")
sf.write(filename+".ogg", data, samplerate)
