"""
  CSC101 - Programming Assignment 1
  9.25 - Traffic Lights
  Sean X.
  Nov. 2nd, 2021

  Summary
"""
import tkinter as tk, tkinter.ttk as ttk


class App(ttk.Frame):
    """App wrapper"""

    def __init__(self, parent):
        """Window title, canvas, and selector"""
        self.parent = parent
        super().__init__(master=self.parent)

        self.winfo_toplevel().title("Traffic Lights")

        # DOC Add traffic lights
        self.trafficLights = TrafficLights(self)
        self.trafficLights.grid(column=1, row=0, rowspan=3)

        # DOC Add selectors
        self.lightSelector = LightSelector(self, self.onSelect)
        self.lightSelector.grid(column=0, columnspan=3, row=3)

        # DOC Make columns equal length
        for col in range(3):
            self.columnconfigure(col, minsize=100)

    def onSelect(self):
        """Update traffic lights"""
        self.trafficLights.changeColor(int(self.lightSelector.store.get()))


class TrafficLights(tk.Canvas):
    """Display the traffic lights and update them"""

    lights = []
    LIGHT_COLORS = ("red", "yellow", "green")

    def __init__(self, parent):
        """Display canvas and create circles"""
        self.parent = parent
        super().__init__(
            master=self.parent,
            width=100,
            height=200,
            background="black",
            highlightthickness=6,
            highlightbackground="gray",
        )

        # DOC Create the three traffic lights
        for i in range(3):
            self.createTrafficLight(56, (i + 1) * 56, 20)

    def createTrafficLight(self, xCord, yCord, radius):
        """Create a circle, https://www.codegrepper.com/code-examples/python/how+to+draw+a+circle+in+tkinter"""
        x1, x2, y1, y2 = (
            xCord - radius,
            xCord + radius,
            yCord - radius,
            yCord + radius,
        )
        self.lights.append(self.create_oval(x1, y1, x2, y2, fill="white"))

    def changeColor(self, lightIndex):
        """Change the color of the traffic light"""
        # DOC Reset the lights
        for light in self.lights:
            self.itemconfig(light, fill="white")

        self.itemconfig(self.lights[lightIndex], fill=self.LIGHT_COLORS[lightIndex])


class LightSelector(ttk.Frame):
    """Select the traffic light to change"""

    class Selector(ttk.Radiobutton):
        """A selector"""

        def __init__(self, parent, name, value, onSelect, store):
            """Create the selector"""
            self.parent = parent
            super().__init__(
                master=self.parent,
                text=name,
                value=value,
                command=onSelect,
                variable=store,
            )

    def __init__(self, parent, onSelect):
        """Display radiobuttons"""
        self.parent = parent
        super().__init__(master=self.parent)

        # DOC Store selection option in a tkinter string variable
        self.store = tk.StringVar()
        for index, color in enumerate(TrafficLights.LIGHT_COLORS):
            self.Selector(self, color.capitalize(), index, onSelect, self.store).grid(
                row=3, column=index
            )
            # DOC Set the minium column width so that the radiobuttons are not squished
            self.columnconfigure(index, minsize=100)


if __name__ == "__main__":
    root = tk.Tk()
    App(root).grid(column=0, row=0)

    # DOC center app, responsive
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # DOC Minium window size
    root.update()  # NOTE Make sure all components are placed, if not placed, winfo will return incorrect values
    root.minsize(root.winfo_width(), root.winfo_height())

    root.mainloop()  # Start event loop
