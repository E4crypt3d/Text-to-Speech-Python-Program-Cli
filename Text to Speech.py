from gtts import gTTS
import os
# By E4crypt3d
user_text= input("Text: ")


while True:
    print("""We will be adding more languages soon...
1. Spanish (United States)
2. English (United States)
3. Mandarin (China Mainland)
4. Portuguese (Portugal)
5. French (France)""")
    user_lang = input("Select your language: ")
    if user_lang == "1":
        language = "es"
        break
    elif user_lang== "2":
        language = "en"
        break
    elif user_lang == "3":
        language = "zh-CN"
        break
    elif user_lang== "4":
        language = "pt"
        break
    elif user_lang== "5":
        language = "fr"
        break
    else:
        print("Please choose a correct option")
audio=gTTS(text=user_text, lang=language,slow=False)

file_name = input("Save as: ")
audio.save(file_name+".mp3")
print("Text Coverted into Audio and Saved")

os.system(file_name+".mp3")
