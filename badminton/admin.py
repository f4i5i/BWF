from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
# Register your models here.
from .models import *


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'player_key')
    search_fields = ('player_id', 'player_key')


class BWFTournamentAdmin(admin.ModelAdmin):
    list_display = ('tourn_id', 'tournament_id',
                    'gender', 'startdate', 'enddate')


class SMatchUrlAdmin(admin.ModelAdmin):
    list_display = ('match_url', 'champ_id')


class TMatchUrlAdmin(admin.ModelAdmin):
    list_display = ('Tmatch_url', 'champ_id')


class EventAdmin(admin.ModelAdmin):
    list_display = ('champ_events', 'event_key')


class PhaseAdmin(admin.ModelAdmin):
    list_display = ('champ_phase', 'phase_key', 'phase_desc',
                    'phase_evkey', 'phase_type')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'tourn_id', 'm_time', 'venue', 'phase')


admin.site.register(Player, PlayerAdmin)
admin.site.register(BWFTournament, BWFTournamentAdmin)
admin.site.register(SMatchUrl, SMatchUrlAdmin)
admin.site.register(TMatchUrl, TMatchUrlAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Match, MatchAdmin)

