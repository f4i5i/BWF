# Generated by Django 3.0.7 on 2020-07-21 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BWFTournament',
            fields=[
                ('tourn_id', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=254)),
                ('m_type', models.CharField(max_length=254)),
                ('startdate', models.CharField(max_length=254)),
                ('enddate', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tournament_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tournamentid', to='players.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('error', models.TextField()),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_key', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('champ_events', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BWFCompEvent', to='badminton.BWFTournament')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.CharField(max_length=254)),
                ('ppstatus', models.CharField(max_length=254)),
                ('m_time', models.CharField(max_length=254)),
                ('venue', models.TextField()),
                ('m_number', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='MatchEvent', to='badminton.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player_key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playermain', to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='TMatchUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tmatch_url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('champ_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BWFTmatchUrls', to='badminton.BWFTournament')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='P1Team', to='badminton.Player')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='P2Team', to='badminton.Player')),
            ],
        ),
        migrations.CreateModel(
            name='SMatchUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('champ_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BWFCompUrls', to='badminton.BWFTournament')),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='AwayPly', to='badminton.Player')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='HomePly', to='badminton.Player')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='SingleMatch', to='badminton.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_key', models.CharField(max_length=254)),
                ('phase_desc', models.CharField(max_length=254)),
                ('phase_evkey', models.CharField(max_length=254)),
                ('phase_type', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('champ_phase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BWFCompPhase', to='badminton.BWFTournament')),
            ],
        ),
        migrations.CreateModel(
            name='MatchScrapingError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.TextField()),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('champ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ChampError', to='badminton.BWFTournament')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='MatchPhase', to='badminton.Phase'),
        ),
        migrations.AddField(
            model_name='match',
            name='tourn_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BWFCompMatch', to='badminton.BWFTournament'),
        ),
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_name', models.CharField(max_length=254)),
                ('draw_type', models.CharField(max_length=254)),
                ('draw_url', models.CharField(max_length=254)),
                ('match_type', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Draw_event_key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='DEkey', to='badminton.Event')),
                ('trn_seas_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tsid', to='players.Tournament_Season')),
            ],
        ),
        migrations.CreateModel(
            name='Double',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('away_T', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='AwayTeam', to='badminton.Team')),
                ('home_T', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='HomeTeam', to='badminton.Team')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='DoubleMatch', to='badminton.Match')),
            ],
        ),
    ]
