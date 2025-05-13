from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(_id=ObjectId(), name='Blue Team', members=[])
        gold_team = Team(_id=ObjectId(), name='Gold Team', members=[])
        blue_team.save()
        gold_team.save()
        for user in users:
            blue_team.members.append(user.email)
            gold_team.members.append(user.email)
        blue_team.save()
        gold_team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0].email, activity_type='Cycling', duration=60, date='2025-05-13T08:00:00Z'),
            Activity(_id=ObjectId(), user=users[1].email, activity_type='Crossfit', duration=120, date='2025-05-13T09:00:00Z'),
            Activity(_id=ObjectId(), user=users[2].email, activity_type='Running', duration=90, date='2025-05-13T10:00:00Z'),
            Activity(_id=ObjectId(), user=users[3].email, activity_type='Strength', duration=30, date='2025-05-13T11:00:00Z'),
            Activity(_id=ObjectId(), user=users[4].email, activity_type='Swimming', duration=75, date='2025-05-13T12:00:00Z'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team='Blue Team', points=100),
            Leaderboard(_id=ObjectId(), team='Gold Team', points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0].email, workout_type='Cycling Training', details={'desc': 'Training for a road cycling event'}, date='2025-05-13T13:00:00Z'),
            Workout(_id=ObjectId(), user=users[1].email, workout_type='Crossfit', details={'desc': 'Training for a crossfit competition'}, date='2025-05-13T14:00:00Z'),
            Workout(_id=ObjectId(), user=users[2].email, workout_type='Running Training', details={'desc': 'Training for a marathon'}, date='2025-05-13T15:00:00Z'),
            Workout(_id=ObjectId(), user=users[3].email, workout_type='Strength Training', details={'desc': 'Training for strength'}, date='2025-05-13T16:00:00Z'),
            Workout(_id=ObjectId(), user=users[4].email, workout_type='Swimming Training', details={'desc': 'Training for a swimming competition'}, date='2025-05-13T17:00:00Z'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
