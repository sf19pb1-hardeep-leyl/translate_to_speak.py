import sys
import os
import playsound
import gtts
import googletrans

print("Enter some text in English and we'll translate and speak it in a different language!")
for key, value in gtts.lang.tts_langs().items():   #a dict
    print(key, value)

print()
lang = input("Please enter the code for your language (e.g., en-us): ")
text = input("Enter some text: ")
print()

translator = googletrans.Translator()
translation = translator.translate(text, src = "en", dest = lang)
print(translation.text)

try:
    textToSpeech = gtts.gTTS(text = translation.text, lang = lang, slow = True)
except BaseException as error:
    print(error, file = sys.stderr)
    sys.exit(1)

# Save the audio in a temporary file with a name.
temporaryFile = tempfile.NamedTemporaryFile()
textToSpeech.save(temporaryFile.name)

# Play and erase the temporary file.
try:
    playsound.playsound(temporaryFile.name, True)   #Requires a filename or URL.
except OSError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
finally:
    temporaryFile.close()   #Erases the temporary file.   

sys.exit(0)
