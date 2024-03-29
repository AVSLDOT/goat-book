from django.test import TestCase
from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")  
        
        self.assertContains(response,"<title>To-Do lists</title>")
        self.assertContains(response,"<html>")
        self.assertContains(response,"</html>")
        
        self.assertContains(response, "<title>To-Do lists</title>") 
        self.assertTemplateUsed(response, "home.html")  
