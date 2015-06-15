from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user goes to website page
        self.browser.get('localhost:8000')

        # user sees that site's title mentions to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # invitation to enter a to-do item straight away
        # user types "Buy peacock feathers " into a text box

        # when user hits enter, the page updates, and now the page lists 
        # "1. Buy peacock feathers" as an item of a to-do list

        # there is still text-box inviting to enter more items.
        # user enters "Use peacock feathers to make a fly"

        # the page updates again, and now both items are shown in the list

        # user wonders, whether the site will remember his list.
        # then he notices that the site has generated a unique url for him 
        # -- there is some explanatory text to that effect

        # user visits that url - his to-do list is still there

        # satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')