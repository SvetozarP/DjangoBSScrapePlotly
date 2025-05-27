from django.db.models import Q
from django.shortcuts import render
from core.models import Fixture
import plotly.express as px
# Create your views here.
def scores(request):
    fixtures = Fixture.objects.all()
    teams = fixtures.values_list('team1', flat=True).distinct()
    scores_sc = {}
    for team in teams:
        team_fixtures = fixtures.filter(Q(team1=team) | Q(team2=team))
        total_score = sum([fix.get_scores(team) for fix in team_fixtures])
        scores_sc[team] = total_score

    scores_sc = dict(sorted(scores_sc.items(), key=lambda x: x[1], reverse=True))

    fig = px.bar(
        x=scores_sc.keys(),
        y=scores_sc.values(),
        title='WRU scores between 29th of Apr 2025 and 27th of May 2025',
        height=800,
    )

    context = {'chart': fig.to_html()}
    return render(request, 'index.html', context)