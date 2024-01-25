import tkinter as tk
from tkinter import messagebox
import random
import calendar
import time
import threading
from tkinter import font

continue_clicked = 0
center_y = 300
def open_news_page():
    def on_continue_clicked():
        global continue_clicked
        global center_y
        continue_clicked+=1
        nonlocal continue_button_clicked
        if not continue_button_clicked:
            messagebox.showinfo("Almost There", "You're doing great!")
            continue_button_clicked = True
        if continue_clicked == 3:
            messagebox.showinfo("Keep Going!", "Things are starting to work...")
            # Update the UI
            update_ui_stage_1()
        elif continue_clicked == 6:
            messagebox.showinfo("Nice Progress!", "Things are looking better now...")
            # Update the UI
            update_ui_stage_2()
        elif continue_clicked == 9:
            messagebox.showinfo("Almost There!", "Just a little more!")
            # Update the UI
            update_ui_stage_3()
        elif continue_clicked == 12:
            messagebox.showinfo("You Got It!", "Well done!")
            # Update the UI
            update_ui_stage_4()
        elif continue_clicked == 15:
            messagebox.showinfo("Fantastic!", "You're on fire!")
            # Update the UI
            update_ui_stage_5()
        elif continue_clicked == 18:
            messagebox.showinfo("Amazing!", "You're unstoppable!")
            # Update the UI
            update_ui_stage_6()
        elif continue_clicked == 21:
            messagebox.showinfo("Incredible!", "No really There is nothing more")
            # Update the UI
            update_ui_stage_7()
        elif continue_clicked == 24:
            messagebox.showinfo("Unbelievable!", "We are really out of budget")
            # Update the UI
            update_ui_stage_8()
        elif continue_clicked == 27:
            messagebox.showinfo("Wow!", "We have been eating bread for weeks now")
            # Update the UI
            update_ui_stage_9()
        elif continue_clicked == 30:
            messagebox.showinfo("Perseverance!", "Some get a peace, some get a crumb")
            # Update the UI
            update_ui_stage_10()
        elif continue_clicked == 33:
            messagebox.showinfo("So Close!", "Please Help")
            # Update the UI
            update_ui_stage_11()
        elif continue_clicked == 36:
            messagebox.showinfo("Just a Little More!", "My adress is")
            # Update the UI
            update_ui_stage_12()
        elif continue_clicked == 39:
            messagebox.showinfo("Almost There!", "Bessemer, AL")
            # Update the UI
            update_ui_stage_13()
        elif continue_clicked == 42:
            messagebox.showinfo("Congratulations!", "You did it!")
            # Update the UI
            update_ui_stage_14()
        elif continue_clicked == 46:
            messagebox.showinfo("Final Stage!", "Im not Sure exactly where we are. We were all enslaved. Please help.")
            # Update the UI
            update_ui_stage_final()

        # Randomly change button size and move closer to the center
        button_width = random.randint(1,10)
        button_height = random.randint(1,10)
        center_x = 400

        button_x = random.randint(center_x - 150, center_x + 150)
        button_y = random.randint(center_y - 50, center_y + 50)
        continue_button.config(width=button_width, height=button_height)
        continue_button.place(x=button_x, y=button_y)

    continue_button_clicked = False

    news_window = tk.Tk()
    news_window.title("Awful News Page")
    news_window.geometry("800x600")
    news_window.resizable(False,False)
    news_window.configure(bg="purple")  # Ugly background color

    # Calendar on top
    calendar_label = tk.Label(news_window, text="Calendar (Not Working)", font=("Helvetica", 24),
                              bg="yellow")  # Random font and color
    calendar_label.pack(pady=20)

    # Scrolling images in the middle (Not Working)
    scroll_label = tk.Label(news_window, text="Scrolling Images (Not Working)", font=("Arial", 20),
                            bg="cyan")  # Random font and color
    scroll_label.pack(pady=50)

    # About text at the bottom
    about_text = """About this Application:
    This application was designed with absolutely no consideration for user experience or aesthetics. \nIt's a showcase of terrible design choices and color combinations.\n We hope you enjoy this painful experience as much as we did in creating it."""

    about_label = tk.Label(news_window, text=about_text, font=("Courier", 12), bg="orange")  # Random font and color
    about_label.pack(pady=10)

    continue_button = tk.Button(news_window, text="Continue", font=("Times New Roman", 12), bg="green", fg="white", command=on_continue_clicked)
    continue_button.pack(pady=10)

    def update_ui_stage_1():

        calendar_label.config(text="Calendar (Almost Working)", font=("Helvetica", 24),
                                  bg="yellow")  # Random font and color
        scroll_label.config(text="Scrolling Images (Not Working)", font=("Arial", 20),
                                bg="cyan")  # Random font and color
        about_label.config(text=about_text, font=("Courier", 12), bg="orange")  # Random font and color


    def update_ui_stage_2():
        calendar_label.config(text="Calendar (Almost Working)", font=("Helvetica", 24),
                              bg="yellow")  # Random font and color
        scroll_label.config(text="Scrolling Images (Almost Working)", font=("Arial", 20),
                            bg="cyan")  # Random font and color
        about_label.config(text=about_text, font=("Courier", 12), bg="orange")  # Random font and color

    def update_ui_stage_3():

        scroll_label.pack_forget()

        about_text = "About this Application: In consideration of the users happiness\nwe removed unnecessary elements from the app\n and focused" \
                     "our skills on the most important parts."
        about_label.config(text=about_text, font=("Courier", 12), bg="orange")  # Random font and color




    def update_ui_stage_4():
        global center_y
        center_y = 100
        def show_calendar():
            year = int(year_entry.get())
            cal_content = calendar.calendar(year)
            cal_label.config(text=cal_content)


        calendar_label.config(text="Calendar Basically Working", font=("Helvetica", 24),
                              bg="yellow")

        year_label = tk.Label(news_window, text="Enter year:")
        year_label.pack(pady=10)
        year_entry = tk.Entry(news_window)
        year_entry.pack(pady=5)

        about_label.pack_forget()
        show_btn = tk.Button(news_window, text="Show Calendar", command=show_calendar)
        show_btn.pack(pady=5)
        # Create the label to display the calendar
        cal_label = tk.Label(news_window, text="", justify="left", font=("Courier New", 10))
        cal_label.pack(pady=10)

    def update_ui_stage_5():
        return 0
    def update_ui_stage_6():
        return 0
    def update_ui_stage_7():
        return 0
    def update_ui_stage_8():
        return 0
    def update_ui_stage_9():
        return 0
    def update_ui_stage_10():
        return 0
    def update_ui_stage_11():
        return 0
    def update_ui_stage_12():
        return 0
    def update_ui_stage_13():
        return 0
    def update_ui_stage_14():
        return 0


    def update_ui_stage_final():
        def my_function():
            for widget in news_window.winfo_children():
                widget.destroy()
            news_window.configure(bg="black")





        def timer_function(delay, func):
            time.sleep(delay)
            func()

        # Create a background thread for the timer_function
        timer_thread = threading.Thread(target=timer_function, args=(4, my_function))
        timer_thread.start()
        return 0
    news_window.mainloop()

def main():
    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            root.destroy()  # Close the login window
            open_news_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    root = tk.Tk()
    root.title("Awful Login Page")
    root.geometry("400x300")
    root.configure(bg="lime")  # Ugly background color

    label_username = tk.Label(root, text="Username", font=("Helvetica", 20), bg="magenta")  # Random font and color
    label_username.pack(pady=20)

    entry_username = tk.Entry(root, font=("Arial", 15), bg="yellow")  # Random font and color
    entry_username.pack(pady=10)

    label_password = tk.Label(root, text="Password", font=("Comic Sans MS", 20), bg="cyan")  # Random font and color
    label_password.pack(pady=20)

    entry_password = tk.Entry(root, font=("Courier", 15), bg="orange")  # Random font and color
    entry_password.pack(pady=10)

    button_login = tk.Button(root, text="Login", font=("Times New Roman", 18), bg="purple", fg="white",
                             command=login)  # Random font and colors
    button_login.pack(pady=20)



    root.mainloop()
main()