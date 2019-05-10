import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome('C:\\Users\\mykeltuz\\Downloads\\Programs\\chromedriver') # change this path to run this test on your device.

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("colors.html"))
        self.assertEqual(driver.title, "Colors")

    def test_red(self):
        driver.get(file_uri("colors.html"))
        red = driver.find_element_by_id("red")
        red.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").value_of_css_property("color"), "rgba(255, 0, 0, 1)")

    def test_blue(self):
        driver.get(file_uri("colors.html"))
        blue = driver.find_element_by_id("blue")
        blue.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").value_of_css_property("color"), "rgba(0, 0, 255, 1)")
    
    def test_green(self):
        driver.get(file_uri("colors.html"))
        green = driver.find_element_by_id("green")
        green.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").value_of_css_property("color"), "rgba(0, 128, 0, 1)")



if __name__ == "__main__":
    unittest.main()
