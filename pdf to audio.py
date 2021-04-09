import pyttsx3
import PyPDF2

book = open('F:/Programming/PYTHON/TTS/NOTES.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(book)

pages = pdfreader.numPages

speaker = pyttsx3.init()

page = pdfreader.getPage(4)

text=page.extractText()
speaker.say(text)
speaker.runAndWait()