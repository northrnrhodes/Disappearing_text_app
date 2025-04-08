from tkinter import *
import threading


class Brains:
    def __init__(self, window):
        # self.window = Tk()
        self.window = window
        self.window.geometry("800x600")
        self.window.title("Disappearing Text App")
        self.window.config(bg='black')
        self.clock = Label(text="Type whatever is on your mind....", font=('Arial', 20, 'normal'), bg='black', fg='white')
        self.clock.pack(pady=20)
        self.entry = Text(width=75, height=25, font=("Arial", 16, 'normal'), bg='black', highlightthickness=0, fg='white')
        self.entry.pack()
        self.entry.focus()
        self.entry.bind('<KeyPress>', self.typing_started)
        self.entry.bind('<KeyRelease>', self.on_key_release)
        self.close = Button(text='QUIT',
                            command=self.close_window,
                            bg='white',
                            highlightthickness=0,
                            borderwidth=0,
                            font=('Arial', 14, 'bold'))

        self.close.config(height=2, width =4)
        self.close.pack()
        self.delay = 500
        self.time_delay = 1000
        self.typing = False
        self.timer = None
        self.typing_timer = None
        # self.window.mainloop()


    def close_window(self):
        if self.timer:
            self.timer.cancel()
        if self.typing_timer:
            self.window.after_cancel(self.typing_timer)
        self.window.destroy()
        print('Program terminated.')


    def typing_finished(self):
        if self.typing == False:
            self.entry.delete("1.0", END)
            print('Text deleted.')
            self.clock.config(text="Type whatever is on your mind....", fg='white')



    def on_key_release(self, event):
        if self.typing_timer is not None:
            self.window.after_cancel(self.typing_timer)

        self.typing_timer = self.window.after(self.delay, self.clear_text)


    def typing_started(self, event):
        self.stop_time = 5
        self.clock.config(text='Typing!', fg='green')

        if self.timer is not None:
            self.timer.cancel()
        self.typing = True



    def clear_text(self):
        self.typing = False
        print('Typing has stopped! Continue typing to prevent your text from disappearing!')
        self.timer = threading.Timer(5.0, self.typing_finished)
        self.timer.start()

        self.delete_timer()



    def delete_timer(self):
        if self.stop_time > 0 and self.typing == False:
            print(f"Count: {self.stop_time}")
            self.clock.config(text=f'Deleting text in {self.stop_time}', fg='red')
            self.stop_time -= 1
            self.window.after(self.time_delay, self.delete_timer)




if __name__ == "__main__":
    window = Tk()
    app = Brains(window)
    window.mainloop()