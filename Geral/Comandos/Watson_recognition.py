# Visa testar o speech_recognition com uma nova API para testes de velocidade
import speech_recognition as sr

# obtain audio from the microphone

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise. One second")
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
    print("Processando...")
    IBM_USERNAME = "apikey"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "e2hAzhi_SxRdYjmDyeA9uTXFkqLmCH9jtEEzCJYm5AHC"  # IBM Speech to Text passwords are mixed-case alphanumeric strings

    # pt-BR_BroadbandModel
    # pt-BR_NarrowbandModel
    try:
        print("Você: " + r.recognize_ibm(audio, language="pt-BR", username=IBM_USERNAME, password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))