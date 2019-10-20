# 用 TTS 產生 RenPy 需要的音檔

RenPy 網址：https://www.renpy.org/

RenPY 說明文檔：https://www.renpy.org/doc/html/

這個專案主要是要用 TTS 的方式產生 RenPy 中的角色對話用的 .ogg 檔。

gvoice.py 可以使用 google TTS 產生 .ogg 檔。不過好像沒有辦法選擇性別。

msvoice.py 會用 MS SAPI5 來產生 .wav 檔，再用 pysoundfile 將 .wav 轉成 .ogg。

執行 yating_zhiwei.reg 可以在 registry 中登錄 Yating 跟 Zhiwei 的聲音，SAPI5 才找的到這兩個聲音。
請參考：http://class.kh.edu.tw/19061/bulletin/msg_view/156

get_voice_name.py 可以列出系統上有那些聲音。

一些免費的 sprites 的下載網址：

https://itch.io/game-assets/free/genre-visual-novel


