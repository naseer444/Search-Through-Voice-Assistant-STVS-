#!/usr/bin/env python
# coding: utf-8

# LIBRARIES WE USED

# In[1]:

import webbrowser as wb
import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pyaudio
import wave

counter1 = 1
counter2 = 0


# TAKE INPUT FROM USER

# In[4]:


def get_voice():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    global counter1

    filename = str(counter1)+'.wav'
    counter1 += 10
    WAVE_OUTPUT_FILENAME = filename

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# SPEAK:

# In[ ]:


def speak(ttx):
    tts = gTTS(text=ttx, lang="en")
    global counter2
    filename = str(counter2) +".mp3"
    counter2+=1
    tts.save(filename)
    playsound.playsound(filename)


# CONVERT VOICE TO TEXT:

# In[5]:


def voice_to_text():
    r = sr.Recognizer()
    # open the file
    name = str(counter1-10)+'.wav'
    with sr.AudioFile(name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text


# TRANSLATION:

# In[ ]:


def Trans(text):
    translator = Translator()
    translation = translator.translate(text,src='ur',dest='en')
    get = translator.translate(translation.text,src='en',dest='ur')
    return get.text


# SEARCH IN ENGLISH:

# In[ ]:


def English():
    speak('What platform you want me to search?')
    speak('Google,Youtube or wikipedia')
    print("SPEAK NOW!!")
    get_voice()
    p_text=voice_to_text()
    if 'Youtube' in p_text:
        speak('What do you want to search on Youtube')
        get_voice()
        q_text=voice_to_text()
        url = 'https://www.youtube.com/results?search_query='
        wb.get().open_new(url + q_text)
    if 'Google' in p_text:
        speak('What do you want to search on Google')
        get_voice()
        q_text=voice_to_text()
        url = 'https://www.google.com/search?q='
        wb.get().open_new(url + q_text)
    if 'Wikipedia' in p_text:
        speak('What do you want to search on Wikipedia')
        get_voice()
        q_text=voice_to_text()
        url ='https://en.wikipedia.org/wiki/Special:Search?search='
        wb.get().open_new(url + q_text)


# SEARCH IN URDU:

# In[ ]:


def Urdu():
    a1=Trans('What platform you want me to search?')
    speak(a1)
    a1=Trans('Google,Youtube or wikipedia')
    speak(a1)
    print("SPEAK NOW!!")
    get_voice()
    p_text=voice_to_text()
    if 'Youtube' in p_text:
        a1=Trans('What do you want to search on Youtube')
        speak(a1)
        get_voice()
        q_text=voice_to_text()
        query=Trans(q_text)
        url = 'https://www.youtube.com/results?search_query='
        wb.get().open_new(url + query)
    if 'Google' in p_text:
        a1=Trans('What do you want to search on Google')
        speak(a1)
        get_voice()
        q_text=voice_to_text()
        query=Trans(q_text)
        url = 'https://www.google.com/search?q='
        wb.get().open_new(url + query)
    if 'Wikipedia' in p_text:
        a1=Trans('What do you want to search on Wikipedia')
        speak(a1)
        get_voice()
        q_text=voice_to_text()
        query=Trans(q_text)
        url ='https://en.wikipedia.org/wiki/Special:Search?search='
        wb.get().open_new(url + query)


# RUNNER:

# In[ ]:


speak('Hello Sir')
speak('What Language you want me to Use')
speak('English or Urdu')
get_voice()
lang = voice_to_text()
if 'English' in lang:
    English()
elif 'Urdu' in lang:
    Urdu()

