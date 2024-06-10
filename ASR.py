import azure.cognitiveservices.speech as speechsdk
import GVF

def use():
    while True:

        # Create a speech configuration
        speech_config = speechsdk.SpeechConfig(subscription=GVF.subscription_key, region=GVF.service_region)
        speech_config.speech_recognition_language = GVF.lang 
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        # Recognize speech from a microphone
        print("Say something...")
        result = speech_recognizer.recognize_once()

        #Check the result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
            input_text = result.text.lower()
            return input_text
            

        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized")
            continue

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            continue
        