import ASR
import ex_TTS
import ChatBot
import GVF
import easyocr
#globale variables
#input_path = "Voices\input.wav"
start_text = ["alpha", "alfa", "alsa","Al."]
end_text = "thank you"
sleep_mode = True
operation_mode = False
language = False
noise = False
non_error = False

while True:
    print("Start Loop")
    #intilaizing 
    input_text = ""
    output_text = ""

    #get text from speech   
    input_text = ASR.use()

    #check sleep mode
    if sleep_mode == True:
        for item in start_text:
            if item in input_text:
                operation_mode = True
                sleep_mode = False
                break
    print(operation_mode)
    #check operation mode
    if operation_mode == True:

        #to generate the input text
        output_text= ChatBot.use(input_text)

        #to convert text to speech
        ex_TTS.use(output_text)
        
        #switch to sleep mode
        if end_text in input_text:
            operation_mode = False
            sleep_mode = True
        print("End of conversation, thanks for using Alpha :)\n")
