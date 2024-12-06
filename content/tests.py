from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from content.models import Category, Content
from users.models import User


class ContentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(phone_number="+7-978-232-02-98")
        self.category = Category.objects.create(name="Dev", description="Как DevOps помогает бизнесу")
        self.content = Content.objects.create(title="Роль DevOps", category=self.category, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_content_retrieve(self):
        url = reverse("content:content_detail", args=(self.content.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_content_create(self):
    #     url = reverse("content:content_create")
    #     self.client.force_login(self.user)
    #     data = {
    #         "title": "Роль DevOps",
    #         "category": self.category.pk,
    #         "content": "Узнайте, как внедрение DevOps помогает бизнесу получать многомиллионную прибыль",
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_302_FOUND)
    #     self.assertEqual(Content.objects.get(title=data.get("title")).title, "Роль DevOps")

    def test_content_update(self):

        url = reverse("content:content_update", args=(self.content.pk,))
        data = {
            "title": "Роль DevOps",
            "category": self.category.pk,
            "content": "Узнайте, как внедрение DevOps помогает бизнесу получать многомиллионную прибыль",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Роль DevOps")

    # def test_content_delete(self):
    #     url = reverse("content:content_delete", args=(self.content.pk,))
    #     self.client.force_login(self.user)
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_302_FOUND)
    #     self.assertEqual(Content.objects.all().count(), 0)

    def test_content_list(self):
        url = reverse("content:content_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
