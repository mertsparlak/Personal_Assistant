import pyautogui
import time
import psutil

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Spotify")
time.sleep(1)
pyautogui.press("enter")

program_name="Spotify.exe"

timeout=time.time() + 120 # 120 sec(2 min)

while True:
    ##spotify açık mı diye kontrol ediyoruz
    for process in psutil.process_iter():
        try:
            if process.name()==program_name:
                print("Spotify is open")
                break
        except(psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    else:
        if time.time()>timeout:
            print("timed out")
            break
        else: 
            #tekrar kontrol etmeden önce küçük bir ara
            time.sleep(1)
            continue
    break
time.sleep(3) ## spotify açılma süresine göre, kendi sistemine göre değiştirebilirsin bu süreyi.
pyautogui.press("space") ## müziği başlatacak

