from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/p-home")
        self.assertEqual(response.status_code, 200)


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/p-about")
        self.assertEqual(response.status_code, 200)
