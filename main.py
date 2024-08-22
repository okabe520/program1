import tkinter as tk
from tkinter import ttk
import math

class Shape:
    def __init__(self, unit='cm'):
        self.unit = unit

    def to_cm(self, value):
        if self.unit == 'in':
            return value * 2.54
        return value

    def get_area(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Square(Shape):
    def __init__(self, side_length, unit='cm'):
        super().__init__(unit)
        self.side_length = self.to_cm(side_length)

    def get_area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, length, width, unit='cm'):
        super().__init__(unit)
        self.length = self.to_cm(length)
        self.width = self.to_cm(width)

    def get_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height, unit='cm'):
        super().__init__(unit)
        self.base = self.to_cm(base)
        self.height = self.to_cm(height)

    def get_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, diameter, unit='cm'):
        super().__init__(unit)
        self.diameter = self.to_cm(diameter)
        self.radius = self.diameter / 2

    def get_area(self):
        return math.pi * (self.radius ** 2)

class AreaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        self.unit_var = tk.StringVar(value='cm')
        self.shape_var = tk.StringVar(value='square')

        self.create_widgets()

    def create_widgets(self):
        # Shape selection
        ttk.Label(self.root, text="Choose the shape:").grid(row=0, column=0, padx=10, pady=10)
        shapes = ['square', 'rectangle', 'triangle', 'circle']
        shape_menu = ttk.Combobox(self.root, textvariable=self.shape_var, values=shapes)
        shape_menu.grid(row=0, column=1, padx=10, pady=10)
        shape_menu.bind("<<ComboboxSelected>>", self.update_form)

        # Unit selection
        ttk.Label(self.root, text="Choose the unit:").grid(row=1, column=0, padx=10, pady=10)
        unit_menu = ttk.Combobox(self.root, textvariable=self.unit_var, values=['cm', 'in'])
        unit_menu.grid(row=1, column=1, padx=10, pady=10)

        # Input fields
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Calculate button
        ttk.Button(self.root, text="Calculate", command=self.calculate_area).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Result display
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.update_form()

    def update_form(self, event=None):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        shape_type = self.shape_var.get()
        if shape_type == 'square':
            ttk.Label(self.input_frame, text="Enter the side length:").grid(row=0, column=0, padx=10, pady=10)
            self.side_entry = ttk.Entry(self.input_frame)
            self.side_entry.grid(row=0, column=1, padx=10, pady=10)

        elif shape_type == 'rectangle':
            ttk.Label(self.input_frame, text="Enter the length:").grid(row=0, column=0, padx=10, pady=10)
            self.length_entry = ttk.Entry(self.input_frame)
            self.length_entry.grid(row=0, column=1, padx=10, pady=10)

            ttk.Label(self.input_frame, text="Enter the width:").grid(row=1, column=0, padx=10, pady=10)
            self.width_entry = ttk.Entry(self.input_frame)
            self.width_entry.grid(row=1, column=1, padx=10, pady=10)

        elif shape_type == 'triangle':
            ttk.Label(self.input_frame, text="Enter the base:").grid(row=0, column=0, padx=10, pady=10)
            self.base_entry = ttk.Entry(self.input_frame)
            self.base_entry.grid(row=0, column=1, padx=10, pady=10)

            ttk.Label(self.input_frame, text="Enter the height:").grid(row=1, column=0, padx=10, pady=10)
            self.height_entry = ttk.Entry(self.input_frame)
            self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        elif shape_type == 'circle':
            ttk.Label(self.input_frame, text="Enter the diameter:").grid(row=0, column=0, padx=10, pady=10)
            self.diameter_entry = ttk.Entry(self.input_frame)
            self.diameter_entry.grid(row=0, column=1, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()















