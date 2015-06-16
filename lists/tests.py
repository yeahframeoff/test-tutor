from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item, List


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        the_list = List()
        the_list.save()
        item1 = Item()
        item1.text = 'The first (ever) list item'
        item1.list = the_list
        item1.save()

        item2 = Item()
        item2.text = 'Item the second'
        item2.list = the_list
        item2.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, the_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_item1 = saved_items[0]
        saved_item2 = saved_items[1]

        self.assertEqual(saved_item1.text, 'The first (ever) list item')
        self.assertEqual(saved_item1.list, the_list)
        self.assertEqual(saved_item2.text, 'Item the second')
        self.assertEqual(saved_item2.list, the_list)


class ListViewTest(TestCase):
    def test_display_all_items(self):
        de_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=de_list)
        Item.objects.create(text='itemey 2', list=de_list)

        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

        self.assertRedirects(response, 
                             '/lists/the-only-list-in-the-world/')
