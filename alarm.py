from datetime import datetime
import sys
import time
import simpleaudio as sa

path = "C:/Users/Marcus/Documents/alarms/Submarine-Klaxon.wav"


wave_obj = sa.WaveObject.from_wave_file(path)
if len(sys.argv) < 4:
    print("Usage: alarm [hour] [minute] [times_to_repeat]")
    exit()
    
alarm_time = datetime.now().replace(hour=int(sys.argv[1]), minute=int(sys.argv[2]), second=0, microsecond=0)

current_time = datetime.now()

while(current_time < alarm_time):
    current_time = datetime.now()
    time.sleep(15)

times_to_repeat = int(sys.argv[3])
while(times_to_repeat > 0):
    play_obj = wave_obj.play()
    play_obj.wait_done()
    times_to_repeat -= 1