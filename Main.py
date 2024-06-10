import ASR
import ex_TTS
import ChatBot
import GVF
import easyocr
#globale variables
#input_path = "Voices\input.wav"
start_text = ["alpha", "alfa", "alsa","Arthur","الفا","السا","الفة","السة"]
end_text = ["thank you","thanks", "thank","thank you.","thanks.", "thank.","شكرا","شكرا لك","شكرا لكي","شكرا.","شكرا لك.","شكرا لكي."]
sleep_mode = True
operation_mode = False
language = False
noise = False
non_error = False


def extract_text_from_image(image_path):
    # Create an OCR reader
    reader = easyocr.Reader(['en'])  # Specify the language(s) you want to support

    # Read text from the image
    result = reader.readtext(image_path)

    # Extracted text is in the 'text' field of each result
    extracted_text = [item[1] for item in result]

    return extracted_text

#lang_detect = input("Welcome, select the language \n   press <1> to Arbic \n    press <2> to English \n :->")
#if lang_detect == "1":
#        GVF.lang = "ar-SA"
#        GVF.voice_name = "ar-SA-ZariyahNeural"


while True:
    print("Start Loop")
    #intilaizing 
    input_text = ""
    output_text = ""

    #get text from speech   
    input_text = ASR.use()

    #Start and check sleep mode
    if sleep_mode == True:
        for item in start_text:
            if item in input_text:
                operation_mode = True
                sleep_mode = False
        else:
            print("not talking with me")
    #End sleep mode

    #start operation mode
    if operation_mode == True:
        #to generate the input text
        output_text= ChatBot.use(input_text)

        #to convert text tp speech
        ex_TTS.use(output_text)
        
        #switch to sleep mode
        for item in end_text:
            if item in input_text:
                operation_mode = False
                sleep_mode = True
                GVF.refresh()
                print("End of conversation, thanks for using Alpha :)\n")

        
