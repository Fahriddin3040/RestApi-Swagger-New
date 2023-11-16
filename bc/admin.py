from django.contrib import admin
from .models import Note, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'f_name', 'l_name', 'password')
    list_display = ('id', 'username', 'registrate_date', 'calculated_balance')
    list_display_links = ('id', 'username')


    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"



@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = ('user', 'category', 'reason', 'price')
    list_display = ('id', 'user', 'category', 'reason', 'price', 'date_time')
    list_display_links = ('id', 'user', )
    filter = ('user', 'category', 'price', 'date_time')
    sortable_by = ('user', 'category', 'price', 'date_time')
