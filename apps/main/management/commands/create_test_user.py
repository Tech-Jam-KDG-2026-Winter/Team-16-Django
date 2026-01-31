# apps/main/management/commands/create_test_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "テスト用ユーザーをまとめて作成"

    def handle(self, *args, **options):
        users = [
            {"username": "test1", "password": "1"},
            {"username": "test2", "password": "2"},
            {"username": "test3", "password": "3"},
        ]

        for u in users:
            if User.objects.filter(username=u["username"]).exists():
                self.stdout.write(f"{u['username']} は既に存在します")
                continue

            User.objects.create_user(
                username=u["username"],
                password=u["password"],
            )
            self.stdout.write(f"{u['username']} を作成しました")
