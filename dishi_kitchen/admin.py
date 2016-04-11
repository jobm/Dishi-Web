from django.contrib import admin
from dishi_kitchen.models import (Kitchen, Recipe,
                                  Menu, Follower, Conversation, ConversationComment,MenuLike)

# Register your models here.
admin.site.register(Kitchen)
admin.site.register(Recipe)
admin.site.register(Menu)
admin.site.register(Follower)
admin.site.register(Conversation)
admin.site.register(ConversationComment)
admin.site.register(MenuLike)
