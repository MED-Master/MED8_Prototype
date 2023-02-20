# MED8_RasaTesting

## **Installation help**

1. **requirements**: Install the requirements
2. **pyaudio**: 
    1. download this file:
    2. name: PyAudio-0.2.11-cp38-cp38-win_amd64.whl and link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
    3. Save the file here: C:\Users\*name* 
    4. pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl

## **How to run the dashboard with Rasa**
1. Run this command in terminal  before executing this program: 
   1. `rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml` 
2. and also run this in seperate terminal 
   1. `rasa run actions`
3. Run the dashboard from the GUI.py file