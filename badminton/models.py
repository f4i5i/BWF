from django.db import models
from players.models import Player,Tournament,Tournament_Season
# Create your models here.


class Player(models.Model):
    player_id = models.CharField(primary_key=True,max_length=200)
    player_key = models.ForeignKey(Player,related_name="playermain",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.player_id


class BWFTournament(models.Model):
    tourn_id = models.CharField(primary_key=True, max_length=254)
    tournament_id = models.ForeignKey(Tournament, related_name="tournamentid", on_delete=models.PROTECT)
    gender = models.CharField(max_length=254)
    m_type = models.CharField(max_length=254)
    startdate = models.CharField(max_length=254)
    enddate = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tourn_id


class SMatchUrl(models.Model):
    match_url = models.TextField()
    champ_id = models.ForeignKey(BWFTournament, related_name="BWFCompUrls", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TMatchUrl(models.Model):
    Tmatch_url = models.TextField()
    champ_id = models.ForeignKey(BWFTournament, related_name="BWFTmatchUrls", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    champ_events = models.ForeignKey(BWFTournament, related_name="BWFCompEvent", on_delete=models.PROTECT)
    event_key = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_key

class Draw(models.Model):
    Draw_event_key = models.ForeignKey(BWFTournament,related_name="DEkey", on_delete=models.PROTECT)
    draw_name = models.CharField(max_length=254)
    draw_type = models.CharField(max_length=254)
    draw_url = models.CharField(max_length=254)
    match_type = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Phase(models.Model):
    champ_phase = models.ForeignKey(BWFTournament, related_name="BWFCompPhase", on_delete=models.PROTECT)
    phase_key = models.CharField(max_length=254)
    phase_desc = models.CharField(max_length=254)
    phase_evkey = models.CharField(max_length=254)
    phase_type = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phase_key


class Match(models.Model):
    match_date = models.CharField(max_length=254)
    tourn_id = models.ForeignKey(BWFTournament, related_name="BWFCompMatch", on_delete=models.PROTECT)
    ppstatus = models.CharField(max_length=254)
    m_time = models.CharField(max_length=254)
    venue = models.TextField()
    m_number = models.CharField(max_length=254)
    event = models.ForeignKey(Event, related_name="MatchEvent", on_delete=models.PROTECT)
    phase = models.ForeignKey(Phase, related_name="MatchPhase", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.match_date


class Team(models.Model):
    player_1 = models.ForeignKey(Player, related_name="P1Team", on_delete=models.PROTECT)
    player_2 = models.ForeignKey(Player, related_name="P2Team", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Single(models.Model):
    home = models.ForeignKey(Player, related_name="HomePly", on_delete=models.PROTECT)
    away = models.ForeignKey(Player, related_name="AwayPly", on_delete=models.PROTECT)
    match = models.ForeignKey(Match, related_name="SingleMatch", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Double(models.Model):
    home_T = models.ForeignKey(Team, related_name="HomeTeam", on_delete=models.PROTECT)
    away_T = models.ForeignKey(Team, related_name="AwayTeam", on_delete=models.PROTECT)
    match = models.ForeignKey(Match, related_name="DoubleMatch", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Error(models.Model):
    url = models.TextField()
    error = models.TextField()
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MatchScrapingError(models.Model):
    error = models.TextField()
    champ = models.ForeignKey(BWFTournament, related_name="ChampError", on_delete=models.PROTECT)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
