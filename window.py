#!/usr/bin/python
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Static Variables
ENTER = 65293
TAB = 65289

# Initialize new builder
builder = Gtk.Builder()
# Specifiy the glade file to load
builder.add_from_file("./terminal.glade")

# Create a new window object from the builder
window = builder.get_object("applicationwindow1")
# Destroy the window and exit this script when the window is closed
window.connect('destroy', Gtk.main_quit)
# Show all the widgets in the window
window.show_all()

# Define the textview objects
Input = builder.get_object("Input")
Output = builder.get_object("Output")


# Parse the input string
def parse_input(text):
    print(text)
    return 0


def tab_autocomplete():
    print("This feature hasn't been added yet")
    # end_iter = Input.get_end_iter()
    # Output.insert(end_iter, "The text to append")


# When the enter key is pressed in the input field
def enter_pressed(widget, event):
    if event.keyval == ENTER:
        # Get the buffer from the Input view
        details = Input.get_buffer()
        # assign the text in the buffer to a string
        text = details.get_text(details.get_start_iter(), details.get_end_iter(), False)
        # Remove all the text in the buffer
        details.set_text("")
        # Parse the input
        return parse_input(text)
    elif event.keyval == TAB:
        tab_autocomplete()


# Connect the textView input to a function
Input.connect('key-press-event', enter_pressed)

# Run the main program
Gtk.main()
