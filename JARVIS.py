import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import webbrowser as wb
from gtts import gTTS
from gtts import lang
from googletrans import Translator
import os
import playsound
import nltk
import re
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
srec = sr.Recognizer()

def get_lang(text):
    word_after_in = text.split("in ")[-1]
    return word_after_in


def find_key_by_value(my_dict, target_value):
    for key, value in my_dict.items():
        if value == target_value.capitalize():
            return key


my_dict = {
  "af": "Afrikaans",
  "ar": "Arabic",
  "bg": "Bulgarian",
  "bn": "Bengali",
  "bs": "Bosnian",
  "ca": "Catalan",
  "cs": "Czech",
  "da": "Danish",
  "de": "German",
  "el": "Greek",
  "en": "English",
  "es": "Spanish",
  "et": "Estonian",
  "fi": "Finnish",
  "fr": "French",
  "gu": "Gujarati",
  "hi": "Hindi",
  "hr": "Croatian",
  "hu": "Hungarian",
  "id": "Indonesian",
  "is": "Icelandic",
  "it": "Italian",
  "iw": "Hebrew",
  "ja": "Japanese",
  "jw": "Javanese",
  "km": "Khmer",
  "kn": "Kannada",
  "ko": "Korean",
  "la": "Latin",
  "lv": "Latvian",
  "ml": "Malayalam",
  "mr": "Marathi",
  "ms": "Malay",
  "my": "Myanmar (Burmese)",
  "ne": "Nepali",
  "nl": "Dutch",
  "no": "Norwegian",
  "pl": "Polish",
  "pt": "Portuguese",
  "ro": "Romanian",
  "ru": "Russian",
  "si": "Sinhala",
  "sk": "Slovak",
  "sq": "Albanian",
  "sr": "Serbian",
  "su": "Sundanese",
  "sv": "Swedish",
  "sw": "Swahili",
  "ta": "Tamil",
  "te": "Telugu",
  "th": "Thai",
  "tl": "Filipino",
  "tr": "Turkish",
  "uk": "Ukrainian",
  "ur": "Urdu",
  "vi": "Vietnamese",
  "zh-CN": "Chinese (Simplified)",
  "zh-TW": "Chinese (Mandarin/Taiwan)",
  "zh": "Chinese (Mandarin)"
}

# target_value = get_lang(text)



    
def speak(audio):
    print('Jarvis',audio)
    engine.say(audio)
    engine.runAndWait()
    

with sr.Microphone() as source:
    print('Listening...')
    audio = srec.listen(source,0,3)
    print('Done')
try:
    text = srec.recognize_google(audio, language='en-in').lower()
    print(f"Jarvies think you said: {text}\n")

    #for youtube
    if text == 'hey jarvis open youtube' or text == 'jarvis youtube':
        print('Jarvis think you said'+' ' + text)

        speak('ok sir')
        webbrowser.open('www.youtube.com')
        speak('opening youtube')
    #for webbrowser    
    elif 'hey jarvis search' in text:
        f_text = 'https://www.google.com/search?q='+text[18:]

        wb.get(chrome_path).open(f_text)
        speak('here what i found')
    #for wikipedia
    elif 'wikipedia' in text.lower():

        speak('searching wikipedia...')
        text = text.replace("wikipedia", "", 1)
        try:
            results = wikipedia.summary(text, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        except wikipedia.PageError:
            print(f"Couldn't find that on Wikipedia.")

    #for calculator
    elif 'hey jarvis open calculator' in text or 'hey jarvis calculator' in text:
        cal = input('calculate here')
        print(eval(cal))

    #for translate language
    elif 'hey jarvis translate' in text:
        text1 = text[20:]
        x = get_lang(text)
        text11 = re.sub(r"in (.*)", "", text1)
        translator = Translator()  
        translate_text = translator.translate(text11,dest = x).text

        text2 = translate_text
        languages = lang.tts_langs()
        
        target_value = get_lang(text)
        key = find_key_by_value(my_dict, target_value)
        language = key
        speech = gTTS(text = text2,lang = language , slow = False)
        speech.save('C://text mp3//new6.mp3')
        playsound.playsound('C://text mp3//new6.mp3')
        
    #open Camera
    elif "hey jarvis open camera" in text or "hey jarvis camera " in text:
        
        cap = cv2.VideoCapture(0)

        while(True):
            ret,frame = cap.read()
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    #recording video
    elif "hey jarvis record video" in text or "hey jarvis record " in text:
        cap = cv2.VideoCapture(0)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter("C:/cv2 video/kf3.mp4",fourc,20,(width,height))

        while True:
            ret,frame = cap.read()
            out.write(frame)
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('x'):
                break
    
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    #crop image   
    elif 'hey jarvis crop' in text or 'hey jarvis crop image' in text:
#         path = input('write path of image')
        img = cv2.imread("C:/image/download.jpg")

        flag = False
        iy = -1
        ix = -1

        def crop(event,x,y,flags,prams):
            global flag,iy,ix

            if event == 1:
                flag = True
                ix = x
                iy = y

            elif event == 4:
                fx = x
                fy = y
                flag = False
                cv2.rectangle(img,pt1 = (ix,iy),pt2 = (x,y),color =(0,0,0),thickness = 1)
                new_img = img[iy:fy,ix:fx]
                cv2.imshow('new_window',new_img)
                cv2.waitKey(0)
        cv2.namedWindow(winname = 'window')
        cv2.setMouseCallback('window',crop)


        while True:
            cv2.imshow('window',img)



            if cv2.waitKey(1) & 0xFF == ord('x'):
                break

        cv2.destroyAllWindows()
        
    # for sending mail   
    elif "hey jarvis send mail" or "hey jarvis send email" in text:
        
        sender_email = "your Email"
        password= 'your generated key from your email'
        speak('please write recievers email')
        receiver_email = input()
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        
        speak('tell your subject')
        with sr.Microphone() as so:
            print('Listening...')
            aud = srec.listen(so,0,6)
            print('done')
            
        sub = srec.recognize_google(aud, language='en-in').lower()
        print(sub)
        message["Subject"] = sub
        
        speak('tell your content')
        with sr.Microphone() as sor:
            print('Listening...')
            audi = srec.listen(sor,0,6)
            print('done')
        
        content = srec.recognize_google(audi,language = 'en-in').lower()
        print(content)
        if 'send' in content:
            body = content[:-4]
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                text = message.as_string()
                server.sendmail(sender_email, receiver_email, text)


        
except Exception as e:
    print(e)
finally:
    speak('thanks sir for using me')



        
