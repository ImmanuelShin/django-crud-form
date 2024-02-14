from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack

class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(title="Chips", description="Tasty chips", purchaser=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Chips")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Chips")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, "Tasty chips")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chips")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args=[str(self.snack.pk)]))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Cookies",
                "description": "Delicious cookies",
                "purchaser": self.user.id,
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("snack_detail", args=[str(self.snack.pk + 1)]))
        self.assertContains(response, "Cookies")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args=[str(self.snack.pk)]),
            {"title": "Updated title", "description": "Yummy update", "purchaser": self.user.id},
        )

        self.assertRedirects(
            response, reverse("snack_detail", args=[str(self.snack.pk)]), target_status_code=200
        )

    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args=[str(self.snack.pk + 1)]),
            {"title": "Updated title", "description": "Yummy update", "purchaser": self.user.id},
        )

        self.assertEqual(response.status_code, 404)

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args=[str(self.snack.pk)]))
        self.assertEqual(response.status_code, 200)

    # you can also test models directly
    def test_model(self):
        snack = Snack.objects.create(title="apple", purchaser=self.user)
        self.assertEqual(snack.title, "apple")
