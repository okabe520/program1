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

    def test_square_area_in_inches(self):
        """
        Test square area calculation with inch inputs.
        """
        self.set_shape('square')
        self.app.unit_var.set('in')
        self.app.side_entry.delete(0, tk.END)
        self.app.side_entry.insert(0, '10')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Area: 645.160 square centimeters")

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

    def test_rectangle_area_in_inches(self):
        """
        Test rectangle area calculation with inch inputs.
        """
        self.set_shape('rectangle')
        self.app.unit_var.set('in')
        self.app.length_entry.delete(0, tk.END)
        self.app.length_entry.insert(0, '10')
        self.app.width_entry.delete(0, tk.END)
        self.app.width_entry.insert(0, '5')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Area: 322.580 square centimeters")

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

    def test_triangle_area_zero_base(self):
        """
        Test triangle area calculation with zero base input.
        """
        self.set_shape('triangle')
        self.app.unit_var.set('cm')
        self.app.base_entry.delete(0, tk.END)
        self.app.base_entry.insert(0, '0')
        self.app.height_entry.delete(0, tk.END)
        self.app.height_entry.insert(0, '5')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "Base and height must be positive.")

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

def test_circle_area_large_diameter(self):
    """
    Test circle area calculation with a very large diameter input.
    """
    self.set_shape('circle')
    self.app.unit_var.set('cm')
    self.app.diameter_entry.delete(0, tk.END)
    self.app.diameter_entry.insert(0, '10000')
    self.app.calculate_area()
    # Allow a small tolerance for floating-point comparison
    result_text = self.app.result_label.cget("text")
    area_value = float(result_text.split()[1])  # Extract area value from string
    self.assertAlmostEqual(area_value, 78539816.339, places=3)


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

    def test_non_numeric_input(self):
        """
        Test non-numeric input handling.
        """
        self.set_shape('circle')
        self.app.unit_var.set('cm')
        self.app.diameter_entry.delete(0, tk.END)
        self.app.diameter_entry.insert(0, 'abc')
        self.app.calculate_area()
        self.assertEqual(self.app.result_label.cget("text"), "could not convert string to float: 'abc'")

    def tearDown(self):
        """
        Clean up after tests.
        """
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()










