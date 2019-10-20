# 用 TTS 產生 RenPy 需要的音檔

gvoice.py 可以使用 google TTS 產生 .ogg 檔。

msvoice.py 會用 MS SAPI5 來產生 .wav 檔，再用 pysoundfile 將 .wav 轉成 .ogg。

執行 yating_zhiwei.reg 可以在 registry 中登錄 Yating 跟 Zhiwei 的聲音，SAPI 才找的到這兩個聲音。
請參考：http://class.kh.edu.tw/19061/bulletin/msg_view/156

get_voice_name.py 可以列出系統上有那些聲音。

一些免費的 sprites 的下載網址：

https://itch.io/game-assets/free/genre-visual-novel


