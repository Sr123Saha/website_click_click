from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import datetime
import time
from pynput import mouse

app = Flask(__name__)
socketio = SocketIO(app)

class ClickCounter:
    def __init__(self):
        self.count = 0

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.count += 1
            socketio.emit('update_clicks', {'count': self.count})
            print(f"\rКоличество кликов: {self.count}  ", end='')

    def start(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

def display_timer(start_time):
    while True:
        elapsed_time = datetime.datetime.now() - start_time
        socketio.emit('update_time', {'elapsed_time': str(elapsed_time)})
        print(f"\rПрошедшее время с запуска программы: {elapsed_time}  ", end='')
        time.sleep(0.0001)

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    

    timer_thread = threading.Thread(target=display_timer, args=(start_time,))
    timer_thread.daemon = True
    timer_thread.start()

    counter = ClickCounter()
    click_thread = threading.Thread(target=counter.start)
    click_thread.daemon = True
    click_thread.start()

    socketio.run(app, debug=True)
