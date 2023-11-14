import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")
        audio = r.listen(source)
        print("Recognizing Now .... ")

        try:
            print("You have said \n" + r.recognize_google(audio))
            text = r.recognize_google(audio)
            print("Audio Recorded Successfully \n ")
            f = open("output.txt", "a")
            f.write(text)
            f.write("\n")
            f.write("\n")
            f.close()
            print("Output Recorded!!")
        except Exception as e:
            print("Error :  " + str(e))


if __name__ == "__main__":
    main()
