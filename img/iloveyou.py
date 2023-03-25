import tkinter as tk

# Define the messages to display
messages = ["Hi love ", "I just wanna say thankyou for always being there whenever i needed you the most", "Im always hoping for the best of us", "Today is  your 18th birthday and i love you so much even" , "the word love cant express how much i feel this for You", "always take care my shining luna<333" ,"-From hiraya, Horacio, Chester Shawn Michael (haba ng name amputa HAHHA)"]
current_message_index = 0

# Define the function to show the next message
def show_next_message():
    global current_message_index
    current_message_index = (current_message_index + 1) % len(messages)
    label.config(text=messages[current_message_index])

# Create the window
window = tk.Tk()

# Create the label widget to display the message
label = tk.Label(window, text=messages[current_message_index])
label.pack()

# Create the button widget to show the next message
button = tk.Button(window, text="<3", command=show_next_message)
button.pack()

# Start the main loop to display the window
window.mainloop()
