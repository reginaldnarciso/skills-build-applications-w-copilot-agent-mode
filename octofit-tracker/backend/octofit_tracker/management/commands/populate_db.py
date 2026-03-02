from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='medium'),
            Workout.objects.create(name='Swimming', description='Swim 1km', difficulty='hard'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='cycle', duration=60, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[3], score=80, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
