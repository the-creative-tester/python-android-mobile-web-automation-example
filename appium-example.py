import unittest
from appium import webdriver

class AndroidWebViewTests(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'Nexus_5',
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def test_mobileweb(self):
        self.driver.get('http://www.google.com')
        # self.driver.find_element(By.NAME, "q").clear()
        self.driver.find_element_by_name('q').clear()
        self.driver.find_element_by_name('q').send_keys('Appium')
        self.driver.find_element_by_name('q').submit()
        # source = self.driver.page_source
        # self.assertNotEqual(-1, source.find('Appium'))

    def tearDown(self):
        self.driver.quit()
