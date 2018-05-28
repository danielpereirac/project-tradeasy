from django.contrib import admin
from .models import User
from .models import Item
from .models import Book
from .models import Card
from .models import Games
from .models import Cloth



class UserModelAdmin(admin.ModelAdmin):
    list_display = ["name","email","created","updated"]
    list_filter = ["name","created","updated"]
    search_fields = ["name", "email"]
    class Meta:
        model = User

admin.site.register(User, UserModelAdmin)
admin.site.register(Item)
# admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Card)
admin.site.register(Games)
admin.site.register(Cloth)