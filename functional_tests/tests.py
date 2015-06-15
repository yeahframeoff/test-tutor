from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user goes to website page
        self.browser.get(self.live_server_url)

        # user sees that site's title mentions to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # invitation to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # user types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when user hits enter, the page updates, and now the page lists 
        # "1: Buy peacock feathers" as an item of a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.check_row_in_list_table('1: Buy peacock feathers')
        
        # there is still text-box inviting to enter more items.
        # user enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, and now both items are shown in the list
        self.check_row_in_list_table('1: Buy peacock feathers')
        self.check_row_in_list_table('2: Use peacock feathers to make a fly')
        
        # user wonders, whether the site will remember his list.
        # then he notices that the site has generated a unique url for him 
        # -- there is some explanatory text to that effect
        self.fail('Finish the test!');

        # user visits that url - his to-do list is still there

        # satisfied, he goes back to sleep
