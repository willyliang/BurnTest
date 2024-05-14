import os
import time
import psutil
import subprocess
import tkinter as tk
from PIL import ImageGrab

# 設定燒機時間（秒）
BURN_TIME = 60

# 截圖保存路徑
SCREENSHOT_DIR = "screenshots"

def burn_cpu():
    print("Burning CPU...")
    start_time = time.time()
    while (time.time() - start_time) < BURN_TIME:
        pass
    print("CPU burning finished.")

def burn_memory():
    print("Burning Memory...")
    process_list = []
    while len(process_list) < psutil.cpu_count():
        process = subprocess.Popen(['python', '-c', 'a = "1" * 1024**3'], shell=True)
        process_list.append(process)
    time.sleep(BURN_TIME)
    for process in process_list:
        process.kill()
    print("Memory burning finished.")

def burn_ssd():
    print("Burning SSD...")
    # 在指定文件夾中建立大容量檔案進行讀寫以模擬硬碟讀寫之情形
    file_path = os.path.join(os.getcwd(), "ssd_burn_test.txt")
    with open(file_path, "wb") as f:
        for _ in range(1024):
            f.write(os.urandom(1024**2))
    time.sleep(BURN_TIME)
    os.remove(file_path)
    print("SSD burning finished.")

def take_screenshot():
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

def display_results():
    # 建立顯示的窗口
    root = tk.Tk()
    root.title("Burn Test Results")

    # 顯示CPU測試結果
    cpu_label = tk.Label(root, text="CPU burning finished.", font=("Helvetica", 12))
    cpu_label.pack()

    # 顯示MEMORY測試結果
    memory_label = tk.Label(root, text="Memory burning finished.", font=("Helvetica", 12))
    memory_label.pack()

    # 顯示SSD測試結果
    ssd_label = tk.Label(root, text="SSD burning finished.", font=("Helvetica", 12))
    ssd_label.pack()

    # 截圖按鈕
    screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
    screenshot_button.pack()

    root.mainloop()

if __name__ == "__main__":
    burn_cpu()
    burn_memory()
    burn_ssd()
    display_results()