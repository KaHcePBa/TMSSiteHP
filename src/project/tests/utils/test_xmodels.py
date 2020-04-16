from unittest import TestCase

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from project.utils.xmodels import a

User = get_user_model()


class Test(TestCase):
    def test_a(self):
        dataset = {
            1: "1",
            None: "None",
            Permission.content_type: "content_type",
            Permission: "auth_permission",
            User.email: "email",
            User.groups: "groups",
            User.id: "id",
            User: "auth_user",
        }

        for data, expected in dataset.items():
            got = a(data)

            self.assertEqual(
                expected, got, f"{a.__name__}({data!r}) -> {got!r} != {expected!r}"
            )
