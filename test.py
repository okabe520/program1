import unittest
from io import StringIO
import sys
import tkinter as tk
from main import Shape, Square, Rectangle, Triangle, Circle, AreaCalculatorApp

class TestAreaCalculatorApp(unittest.TestCase):

    def setUp(self):
        """
        Set up the GUI for testing.
        """
        self.root = tk.Tk()
        self.app = AreaCalculatorApp(self.root)
        self.root.update()  # Update the GUI to make sure everything is initialized

    def set_shape(self, shape_type):
        """
        Helper method to set the shape type and update the form.
        """
        self.app.shape_var.set(shape_type)
        self.app.update_form()
        self.root.update()  # Ensure GUI updates

    def test_square_area(self):
        """
        Test square area calculation with various valid and invalid inputs.
        """
        self.set_shape('square')
        self.app.unit_var.set('cm')
        self.app.side_entry.delete(0, tk.END)
        self.app.side_entry.insert(0, '10')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Area: 100.000 square centimeters")

    def test_rectangle_area(self):
        """
        Test rectangle area calculation with various valid and invalid inputs.
        """
        self.set_shape('rectangle')
        self.app.unit_var.set('cm')
        self.app.length_entry.delete(0, tk.END)
        self.app.length_entry.insert(0, '10')
        self.app.width_entry.delete(0, tk.END)
        self.app.width_entry.insert(0, '5')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Area: 50.000 square centimeters")

    def test_triangle_area(self):
        """
        Test triangle area calculation with various valid and invalid inputs.
        """
        self.set_shape('triangle')
        self.app.unit_var.set('cm')
        self.app.base_entry.delete(0, tk.END)
        self.app.base_entry.insert(0, '10')
        self.app.height_entry.delete(0, tk.END)
        self.app.height_entry.insert(0, '5')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Area: 25.000 square centimeters")

    def test_circle_area(self):
        """
        Test circle area calculation with various valid and invalid inputs.
        """
        self.set_shape('circle')
        self.app.unit_var.set('cm')
        self.app.diameter_entry.delete(0, tk.END)
        self.app.diameter_entry.insert(0, '10')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Area: 78.540 square centimeters")

    def test_invalid_input(self):
        """
        Test invalid input handling.
        """
        self.set_shape('square')
        self.app.unit_var.set('cm')
        self.app.side_entry.delete(0, tk.END)
        self.app.side_entry.insert(0, '-10')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Side length must be positive.")

    def tearDown(self):
        """
        Clean up after tests.
        """
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()









