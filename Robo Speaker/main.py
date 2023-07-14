import pyttsx3


def robo_speaker():
    print("Welcome to the Robo Speaker")
    print("Developed by Talha Khalid")

    while 1:
        x = input("What do you want me to speak: ")

        tk = pyttsx3.init()
        tk.say(x)
        tk.runAndWait()

        if x == 'stop':
            tk = pyttsx3.init()
            tk.say("Ok, now i will stop executing the code...")
            tk.runAndWait()
            break


robo_speaker()

