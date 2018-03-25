# -*- coding: utf-8 -*-
import TextToSpeech, PlayTape, BotConnection, SpeechToText, Main,SpeechConfig

def ListeningMode():
   print 'listening mode'
   tempSpeechText = SpeechToText.startSpeech()
   return tempSpeechText

def ProcessingMode(tempText):
   print 'processing mode'
   myresponse = BotConnection.connectBot(tempText)

   return myresponse

def RecordingMode(tempResponse):
   print 'recording mode'
   tapeName = TextToSpeech.recordTextToSpeech(tempResponse)

   return tapeName

def SpeakingMode(tempTapePath):
   print 'speaking mode'
   try:
       PlayTape.playTape(tempTapePath)
   except Exception as e:
       print 'There is no file to play'
       print e


def autoMode():
   tempSpeechText=ListeningMode()
   tempResponse=ProcessingMode(tempSpeechText)
   tempTapePath=RecordingMode(tempResponse)
   SpeakingMode(tempTapePath)

def souffleMode_threaded(tempSouffleText): # içeride input almak istersen unicode'a çevirmeyi unutma... !!! tempSouffleText mobil cihazdan gelecek aslında...
   print 'waiting for input'
   tempSouffleText = raw_input()
   tempSouffleText = unicode(tempSouffleText,"utf-8")
   souffle=RecordingMode(tempSouffleText)
   SpeakingMode(souffle)


# ilk parametre operations fonksiyonu içindeki kontrollere girmek için.
# ikinci parametre dictionary'den fonksiyonu seçen key için.
def operations(key, option,parameter=""):
    multiSelection(key,option,parameter)


def multiSelection(key,op,parameter):
    if key == 0: # autoMode()
        funDict[op]()
    elif key == 1: # souffleMode(p)
        funDict[op](parameter)
    elif key == 2: # ListeningMode()
        funDict[op]()
    elif key == 3: # ProcessingMode(p)
        funDict[op](parameter)
    elif key == 4: # RecordingMode(p)
        funDict[op](parameter)
    elif key == 5: # SpeakingMode(p)
        funDict[op](parameter)



funDict = {
    0: autoMode,
    1: souffleMode_threaded,
    2: ListeningMode,
    3: ProcessingMode,
    4: RecordingMode,
    5: SpeakingMode,

}

if __name__ == '__main__':
    # Speaking Mode ->  operations(5, 5,'records/systemrecords/myrecord.mp3')
    operations(0,0)
    # souffle Mode ->operations(1,1,'nasılsınız')