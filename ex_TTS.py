import azure.cognitiveservices.speech as speechsdk
import GVF

output_path = "Voices\output.wav"

def use(output_text):
    
    #convert text to speech
    state = True
    speech_config = speechsdk.SpeechConfig(subscription=GVF.subscription_key, region=GVF.service_region)
    speech_config.speech_synthesis_voice_name = GVF.voice_name
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    #result = synthesizer.speak_text_async(output_text).get()
    result = synthesizer.speak_text(output_text)

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Successfully synthesized the audio to speech with the selected voice.")
    else:
        print("Speech synthesis failed: {}".format(result.reason))
        state = False

    # Save the synthesized audio to a file
    audio_data = result.audio_data
    with open(output_path, "wb") as audio_file:
        audio_file.write(audio_data)
    return state


