# Transcriptor/Traductor

![Logo Python](https://img.shields.io/pypi/pyversions/Django?color=w&logo=python&logoColor=yellow)<br>
**SPA** - Programa en Python que escucha en bucle por el micrófono del dispositivo. En cada pausa, el programa transcribirá lo que se acaba de decir y lo traducirá al
español, mostrando ambos textos. Su funcionamiento es el siguiente:<br>
1. El programa entra en un bucle en el que está escuchando constantemente (hasta que el usuario diga *"exit"*).
2. Esto va generando un archivo de audio que es transformado en una *string* mediante el conversor de Google.
3. Esta *string* es mandada a consola. También es mandada la cadena traducida por el traductor de Google.
4. Se repite el proceso hasta que el usuario diga *"exit"*.
<br>

**EN** - Python program that listens in a loop through the device's microphone. At each pause, the program will transcribe what has just been said and translate it into
Spanish, showing both texts. Its operation is as follows:<br>
1. The program goes into a loop where it is constantly listening (until the user says "exit").
2. This is generating an audio file that is converted to a string using Google's converter.
3. This string is sent to the console. The string translated by Google translate is also sent.
4. The process is repeated until the user says "exit".
