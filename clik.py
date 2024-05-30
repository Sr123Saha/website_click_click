from pynput import mouse
import time
import datetime
import threading

class ClickCounter:
    def __init__(self):
        self.count = 0

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.count += 1
            print(f"\rКоличество кликов: {self.count}  ", end='')

    def start(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

def display_timer(start_time):
    while True:
        elapsed_time = datetime.datetime.now() - start_time
        print(f"\rПрошедшее время с запуска программы: {elapsed_time}  ", end='')
        time.sleep(1)

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    
    # Запускаем поток для таймера
    timer_thread = threading.Thread(target=display_timer, args=(start_time,))
    timer_thread.daemon = True
    timer_thread.start()

    # Создаем и запускаем счетчик кликов
    counter = ClickCounter()
    
    print("Начинаю отслеживать клики и показывать время. Нажмите Ctrl+C для выхода.")
    try:
        counter.start()
    except KeyboardInterrupt:
        final_time = datetime.datetime.now() - start_time
        print(f"\nФинальное количество кликов: {counter.count}")
        print(f"Общее время работы программы: {final_time}")
        print("Программа завершена.")
