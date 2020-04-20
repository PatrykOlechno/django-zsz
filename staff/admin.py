from django.contrib import admin
from staff.models import Member, Position, Cadence

class PositionInLine(admin.TabularInline):
    model = Position
    extra = 2


class CadenceInLine(admin.TabularInline):
    model = Cadence
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ( 'name',)

    inlines = [
        PositionInLine,
        CadenceInLine,
    ]

admin.site.register(Member, MemberAdmin)
