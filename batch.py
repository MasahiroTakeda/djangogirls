from django.utils import timezone

from ...models import Post

        # print(Post)
        today = timezone.localtime(timezone.now()).date()
        # today = timezone.now().date()
        yesterday = today + timezone.timedelta(days=-1)

        print(today)
        print(yesterday)

        posts = Post.objects.filter(
            published_date__lte=timezone.now(),
            created_date__gte=yesterday
            # created_date__gt=yesterday
        ).order_by('published_date')
        print(posts)