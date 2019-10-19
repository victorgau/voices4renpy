import mstts
import soundfile as sf

mstts.get_name()

filename = "hanhan"
mstts.create(name="Hanhan", 
             filename=filename+".wav",
             message="可是他線在水很髒！臭死了！", 
             rate=0, 
             volume=100)

# 使用 PySoundFile 把 .wav 檔，轉成 .ogg 檔
data, samplerate = sf.read(filename+".wav")
sf.write(filename+".ogg", data, samplerate)
