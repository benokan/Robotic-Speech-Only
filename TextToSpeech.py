# -*- coding: utf-8 -*-
from gtts import gTTS
import os,SpeechConfig

# recordTextToSpeech(myresponse) function takes the argument "myresponse" and
# it records bot's response as a mp3 type and it returns the name of tape.
def recordTextToSpeech(myresponse):
    try :
        mywords = (myresponse)

        tts = gTTS(text=mywords, lang='tr')
        path = str(SpeechConfig.Tape_Record_Folder + ".mp3")
        tts.save(path)
    except Exception:
        path=SpeechConfig.TextToSpeechTempAudio1
    finally:
        return path


# calling deleteAllRecords() function before our infinite loop to avoid overflow...
def deleteAllRecords():
    dirPath = "records"
    fileList = os.listdir(dirPath)
    try:
        for FileName in fileList:
            os.remove(dirPath + "/" + FileName)
    except: Exception

    finally: pass

if __name__ == '__main__':
    print("Calling External Text To Speech Main")
