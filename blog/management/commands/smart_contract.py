# -*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import Post


class Command(BaseCommand):
    help = '記事が一件でも投稿されていない場合は、スマートコントラクトを実行する。'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Run Smart Contract Command!'))
        self.stdout.write(options.__str__())

        today = timezone.localtime(timezone.now()).date()
        yesterday = today + timezone.timedelta(days=-1)

        print('today : ', today)
        print('yesterday : ', yesterday)

        posts = Post.objects.filter(
            published_date__lte=timezone.now(),
            created_date__gte=yesterday,
            created_date__lte=today
        ).order_by('-published_date')
        print(posts)

        # 記事が一件も無い場合はスマートコントラクトを実行
        if not posts:
            self.smart_contract()

    def smart_contract(self):
        """スマートコントラクトを叩く処理を実行
        """
        print(self)

        # web3.pyを使用して、スマートコントラクトを実行する処理を書く　
        print('smart contract !!')
