from django.contrib import admin
from .models import Item
from .models import Book
from .models import Card
from .models import Games
from .models import Cloth


admin.site.register(Book)
admin.site.register(Card)
admin.site.register(Games)
admin.site.register(Cloth)