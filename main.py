
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Caitlin Bank")

# Add a label
welcome = tk.Label(window, text="Welcome to your bank account!")
choice1 = tk.Button(window, text="1) View account balance")
choice2 = tk.Button(window, text="2) Make withdrawal")
choice3 = tk.Button(window, text="3) Make deposit")
choice4 = tk.Button(window, text="4) Exit")

welcome.pack()

# Add a button
choice1.pack()
choice2.pack()
choice3.pack()
choice4.pack()


# Start the Tkinter event loop
window.mainloop()
