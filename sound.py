from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language='en'
sp =gTTS(text ="Mardchod gandu lavdya bhenchod lavdu teri maa ki chut    "
, lang= language,slow=False)
sp.save(audio)
playsound(audio)
