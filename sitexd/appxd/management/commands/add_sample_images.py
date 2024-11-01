import random
from django.core.management.base import BaseCommand
from appxd.models import Image, Rectangle

class Command(BaseCommand):
    help = 'Add sample images to the database'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='The total number of sample images to add')

    def handle(self, *args, **options):
        total = options['total']

        sample_title = 'sample image'

        for _ in range(total):
            title = sample_title
            width = random.randint(100, 500)
            height = random.randint(100, 500)
            image = Image.objects.create(title=title, width=width, height=height)

            num_rectangles = random.randint(1, 5)
            for _ in range(num_rectangles):
                x = random.randint(0, width - 50)
                y = random.randint(0, height - 50)
                rect_width = random.randint(10, 50)
                rect_height = random.randint(10, 50)
                fill_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))

                Rectangle.objects.create(image=image, x=x, y=y, width=rect_width, height=rect_height, fill_color=fill_color)

        self.stdout.write(self.style.SUCCESS(f'{total} sample images added successfully'))
    
    # python manage.py add_sample_images
