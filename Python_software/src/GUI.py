import tkinter as tk
import PyQt5
import pyttsx3

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from util import *
from shortcuts import *
import json

engine = pyttsx3.init()


class ShortcutsGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Shortcuts')

        self.label = tk.Label(self.root, text="Shortcuts", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Start to Translate \nto Braille", font=('Arial', 14), command = self.TranslateToBraille)
        self.btn1.place(x= 100, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Enable Braille Display", font=('Arial', 14), command = self.EnableBrailleDisplay)
        self.btn2.place(x= 350, y = 100, height = 100, width = 200)

        self.btn3 = tk.Button(self.root, text="Toggle Navigation", font=('Arial', 14), command = self.ToggleNavigation)
        self.btn3.place(x= 600, y = 100, height = 100, width = 200)

        self.btn4 = tk.Button(self.root, text="Accessibility", font=('Arial', 14), command = self.Accessibility)
        self.btn4.place(x= 100, y = 250, height = 100, width = 200)

        self.btn5 = tk.Button(self.root, text="Index Up", font=('Arial', 14), command = self.IndexUp)
        self.btn5.place(x= 350, y = 250, height = 100, width = 200)

        self.btn6 = tk.Button(self.root, text="Index Down", font=('Arial', 14), command = self.IndexDown)
        self.btn6.place(x= 600, y = 250, height = 100, width = 200)

        self.btn7 = tk.Button(self.root, text="Text to Speech", font=('Arial', 14), command = self.TextToSpeech)
        self.btn7.place(x= 100, y = 400, height = 100, width = 200)

        self.btn8 = tk.Button(self.root, text="Quit Translation", font=('Arial', 14), command = self.QuitTranslation)
        self.btn8.place(x= 350, y = 400, height = 100, width = 200)

        self.btn9 = tk.Button(self.root, text="Continue Translation", font=('Arial', 14), command = self.ContinueTranslation)
        self.btn9.place(x= 600, y = 400, height = 100, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Settings", font = ('Arial', 12), command = self.ReturnToSettings)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        engine.say("Opening Shortcuts")
        engine.runAndWait()
        self.root.mainloop()


    def TranslateToBraille(self):
        self.root.destroy()
        TranslateToBraille()
    
    def EnableBrailleDisplay(self):
        self.root.destroy()
        EnableBrailleDisplay()

    def ToggleNavigation(self):
        self.root.destroy()
        ToggleNavigation()

    def Accessibility(self):
        self.root.destroy()
        Accessibility()

    def IndexUp(self):
        self.root.destroy()
        IndexUp()

    def IndexDown(self):
        self.root.destroy()
        IndexDown()

    def TextToSpeech(self):
        self.root.destroy()
        TextToSpeech()

    def QuitTranslation(self):
        self.root.destroy()
        QuitTranslation()

    def ContinueTranslation(self):
        self.root.destroy()
        ContinueTranslation()

    def ReturnToSettings(self):
        self.root.destroy()
        SettingsGUI()

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Main Menu')

        self.label = tk.Label(self.root, text="Main Menu", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Settings", font=('Arial', 14), command = self.OpenSettings)
        self.btn1.place(x= 350, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Open Browser", font=('Arial', 14), command = self.OpenBrowser)
        self.btn2.place(x= 350, y = 250, height = 100, width = 200)

        self.btn3 = tk.Button(self.root, text="Modes", font=('Arial', 14), command = self.OpenModes)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

        engine.say("Opening Main Menu")
        engine.runAndWait()

        self.root.mainloop()


    def OpenSettings(self):
        self.root.destroy()
        SettingsGUI()

    def OpenModes(self):
        self.root.destroy()
        ModesGUI()

    def OpenBrowser(self):
        print(getBrowserOpen())
        if (getBrowserOpen() == False):
            on_triggered()

class SettingsGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Settings')

        self.label = tk.Label(self.root, text="Settings", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Shortcuts", font=('Arial', 14), command = self.OpenShortcuts)
        self.btn1.place(x= 350, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Speech Speed", font=('Arial', 14), command = self.OpenSpeeds)
        self.btn2.place(x= 350, y = 250, height = 100, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Main Menu", font = ('Arial', 12), command = self.ReturnToMain)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        engine.say("Opening Settings")
        engine.runAndWait()
        self.root.mainloop()


    def OpenShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

    def ReturnToMain(self):
        self.root.destroy()
        MainMenu()

    def OpenSpeeds(self):
        self.root.destroy()
        SpeechSpeedGUI()

class ModesGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Modes')

        self.label = tk.Label(self.root, text="Modes", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Assistantive Mode", font=('Arial', 14))
        self.btn1.place(x= 350, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Individual Mode\n(Automatic)", font=('Arial', 14))
        self.btn2.place(x= 350, y = 250, height = 100, width = 200)

        self.btn3 = tk.Button(self.root, text="Individual Mode\n(Manual)", font=('Arial', 14))
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Main Menu", font = ('Arial', 12), command = self.ReturnToMain)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        engine.say("Opening Modes")
        engine.runAndWait()
        self.root.mainloop()



    def ReturnToMain(self):
        self.root.destroy()
        MainMenu()
    
class TranslateToBraille:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Start Translate To Braille", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["readBraille"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Braille Translate shortcut is " + shortcut["readBraille"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

        

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : self.ShortcutEntry.get(),
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class EnableBrailleDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Enable Braille Display", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["activateArduino"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Enable Braille Display shortcut is " + shortcut["activateArduino"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : self.ShortcutEntry.get(),
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class ToggleNavigation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Toggle Navigation", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["navigation"])
        
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Toggle Navigation shorcut is " + shortcut["navigation"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": self.ShortcutEntry.get(),
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class Accessibility:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Accessibility", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["accessibility"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)
        
        engine.say("Accessibility shorcut is " + shortcut["accessibility"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": self.ShortcutEntry.get(),
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class IndexUp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Index Up", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["indexPlus"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Index up shortcut is " + shortcut["indexPlus"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": self.ShortcutEntry.get(),
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class IndexDown:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Index Down", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["indexMinus"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Index down shortcut is " + shortcut["indexMinus"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : self.ShortcutEntry.get(),
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class TextToSpeech:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Text To Speech", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["speak"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Text to Speech shortcut is " + shortcut["speak"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : self.ShortcutEntry.get(),
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class QuitTranslation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Quit Translation", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["brailleQuit"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Quit Translation shortcut is " + shortcut["brailleQuit"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : self.ShortcutEntry.get(),
            "brailleContiue": shortcut["brailleContiue"],
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class ContinueTranslation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Controls')

        self.label = tk.Label(self.root, text="Continue Translation", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.backBtn = tk.Button(self.root, text = "< Shortcuts", font = ('Arial', 12), command = self.ReturnToShortcuts)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        shortcut  = read_shortcut()
        var = tk.StringVar()
        var.set(shortcut["brailleContiue"])
        self.ShortcutEntry = tk.Entry(self.root, textvariable=var, font=('Arial', 16))
        self.ShortcutEntry.place(x= 350, y = 250, height = 100, width = 200)

        engine.say("Continue Translation shortcut is " + shortcut["brailleContiue"])
        engine.runAndWait()

        self.btn3 = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

    def onSave(self):
        shortcut  = read_shortcut()
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": self.ShortcutEntry.get(),
            "speed": shortcut["speed"]
        }
        write_json(data)

    def ReturnToShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

class SpeechSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Speed Settings')

        self.label = tk.Label(self.root, text="Speech Speed", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Slow", font=('Arial', 14), command = self.SlowSpeed, bg='tomato')
        self.btn1.place(x= 100, y = 250, height = 200, width = 200)

        self.btn2 = tk.Button(self.root, text="Medium", font=('Arial', 14), command = self.MediumSpeed, bg='gold')
        self.btn2.place(x= 350, y = 250, height = 200, width = 200)

        self.btn3 = tk.Button(self.root, text="Fast", font=('Arial', 14), command = self.FastSpeed, bg='SpringGreen2')
        self.btn3.place(x= 600, y = 250, height = 200, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Settings", font = ('Arial', 12), command = self.ReturnToSettings)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)


        shortcut  = read_shortcut()
        self.var = tk.StringVar()
        self.var.set(shortcut["speed"])
        self.label2 = tk.Label(self.root, textvariable=self.var, font=('Arial', 18))
        self.label2.place(x=500, y = 100)

        self.label3 = tk.Label(self.root, text = "Current Speed: ", font=('Arial', 18))
        self.label3.place(x=300, y = 100)

        self.SaveButton = tk.Button(self.root, text="Save", font=('Arial', 14), bg='green', command=self.onSave)
        self.SaveButton.place(x= 350, y = 480, height = 100, width = 200)

        engine.say("Opening Speech Speed Settings")
        engine.runAndWait()
        self.root.mainloop()

    def SlowSpeed(self):
        shortcut  = read_shortcut()
        speed = 30
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": speed
        }
        write_json(data)
        self.var.set(shortcut["speed"])

    def MediumSpeed(self):
        shortcut  = read_shortcut()
        speed = 60
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": speed
        }
        write_json(data)
        self.var.set(shortcut["speed"])

    def FastSpeed(self):
        shortcut  = read_shortcut()
        speed = 90
        data = {
            "readBraille" : shortcut["readBraille"],
            "activateArduino" : shortcut["activateArduino"],
            "navigation": shortcut["navigation"],
            "accessibility": shortcut["accessibility"],
            "hierarchy" : shortcut["hierarchy"],
            "indexMinus" : shortcut["indexMinus"],
            "indexPlus": shortcut["indexPlus"],
            "speak" : shortcut["speak"],
            "brailleQuit" : shortcut["brailleQuit"],
            "brailleContiue": shortcut["brailleContiue"],
            "speed": speed
        }
        write_json(data)
        self.var.set(shortcut["speed"])

    def onSave(self):
        shortcut  = read_shortcut()
        self.var.set(shortcut["speed"])
        self.label2.update

    def ReturnToSettings(self):
        self.root.destroy()
        SettingsGUI()