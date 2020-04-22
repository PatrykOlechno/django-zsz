from django.contrib import admin
from staff.models import Member, Position, Cadence

class PositionInLine(admin.TabularInline):
    model = Position
    extra = 1

class CadenceInLine(admin.TabularInline):
    model = Cadence
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ( 'name', 'get_cadences', 'get_positions')
    list_filter = ['cadence', 'degree']
    search_field = ['name']

admin.site.register(Member, MemberAdmin)
admin.site.register(Cadence)
admin.site.register(Position)
