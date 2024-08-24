import tkinter as tk
from tkinter import ttk
import math

class Shape:
    """
    A base class for shapes that calculates area.

    Attributes:
        unit (str): The unit of measurement, either 'cm' or 'in'.
    """

    def __init__(self, unit='cm'):
        """
        Initializes the shape with the given unit.

        Args:
            unit (str): The unit of measurement, defaults to 'cm'.
        """
        self.unit = unit

    def to_cm(self, value):
        """
        Converts the measurement to centimeters if the unit is 'in'.

        Args:
            value (float): The measurement value.

        Returns:
            float: The converted measurement in centimeters.
        """
        if self.unit == 'in':
            return value * 2.54
        return value

    def get_area(self):
        """
        Calculates the area of the shape. This method should be overridden by subclasses.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses should implement this method.")

class Square(Shape):
    """
    A class representing a square.

    Attributes:
        side_length (float): The length of the square's side.
    """

    def __init__(self, side_length, unit='cm'):
        """
        Initializes the square with a given side length and unit.

        Args:
            side_length (float): The length of the square's side.
            unit (str): The unit of measurement, defaults to 'cm'.
        """
        super().__init__(unit)
        self.side_length = self.to_cm(side_length)

    def get_area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.side_length ** 2

class Rectangle(Shape):
    """
    A class representing a rectangle.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    """

    def __init__(self, length, width, unit='cm'):
        """
        Initializes the rectangle with a given length, width, and unit.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
            unit (str): The unit of measurement, defaults to 'cm'.
        """
        super().__init__(unit)
        self.length = self.to_cm(length)
        self.width = self.to_cm(width)

    def get_area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
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

    def calculate_area(self):
        shape_type = self.shape_var.get()
        unit = self.unit_var.get()

        try:
            if shape_type == 'square':
                side_length = float(self.side_entry.get())
                if side_length <= 0:
                    raise ValueError("Side length must be positive.")
                shape = Square(side_length, unit)
            elif shape_type == 'rectangle':
                length = float(self.length_entry.get())
                width = float(self.width_entry.get())
                if length <= 0 or width <= 0:
                    raise ValueError("Length and width must be positive.")
                shape = Rectangle(length, width, unit)
            elif shape_type == 'triangle':
                base = float(self.base_entry.get())
                height = float(self.height_entry.get())
                if base <= 0 or height <= 0:
                    raise ValueError("Base and height must be positive.")
                shape = Triangle(base, height, unit)
            elif shape_type == 'circle':
                diameter = float(self.diameter_entry.get())
                if diameter <= 0:
                    raise ValueError("Diameter must be positive.")
                shape = Circle(diameter, unit)
            else:
                self.result_label.config(text="Invalid shape!")
                return

            area = shape.get_area()
            self.result_label.config(text=f"Area: {area:.3f} square centimeters")

        except ValueError as e:
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()















