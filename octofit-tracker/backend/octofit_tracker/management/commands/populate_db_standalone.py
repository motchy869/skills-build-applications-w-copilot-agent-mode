from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta

# MongoDB接続
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# 既存データ削除
for col in ['users', 'teams', 'activity', 'leaderboard', 'workouts']:
    db[col].drop()

# ユーザー作成
users = [
    {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "thundergod", "password": "thundergodpassword"},
    {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "metalgeek", "password": "metalgeekpassword"},
    {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "zerocool", "password": "zerocoolpassword"},
    {"_id": ObjectId(), "email": "crashoverride@hmhigh.edu", "name": "crashoverride", "password": "crashoverridepassword"},
    {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "sleeptoken", "password": "sleeptokenpassword"},
]
db.users.insert_many(users)

# チーム作成
blue_team = {"_id": ObjectId(), "name": "Blue Team", "members": [u["email"] for u in users]}
gold_team = {"_id": ObjectId(), "name": "Gold Team", "members": [u["email"] for u in users]}
db.teams.insert_many([blue_team, gold_team])

# アクティビティ作成
activities = [
    {"_id": ObjectId(), "user": users[0]["email"], "activity_type": "Cycling", "duration": 60, "date": datetime(2025, 5, 13, 8, 0)},
    {"_id": ObjectId(), "user": users[1]["email"], "activity_type": "Crossfit", "duration": 120, "date": datetime(2025, 5, 13, 9, 0)},
    {"_id": ObjectId(), "user": users[2]["email"], "activity_type": "Running", "duration": 90, "date": datetime(2025, 5, 13, 10, 0)},
    {"_id": ObjectId(), "user": users[3]["email"], "activity_type": "Strength", "duration": 30, "date": datetime(2025, 5, 13, 11, 0)},
    {"_id": ObjectId(), "user": users[4]["email"], "activity_type": "Swimming", "duration": 75, "date": datetime(2025, 5, 13, 12, 0)},
]
db.activity.insert_many(activities)

# リーダーボード作成
leaderboard = [
    {"_id": ObjectId(), "team": "Blue Team", "points": 100},
    {"_id": ObjectId(), "team": "Gold Team", "points": 90},
]
db.leaderboard.insert_many(leaderboard)

# ワークアウト作成
workouts = [
    {"_id": ObjectId(), "user": users[0]["email"], "workout_type": "Cycling Training", "details": {"desc": "Training for a road cycling event"}, "date": datetime(2025, 5, 13, 13, 0)},
    {"_id": ObjectId(), "user": users[1]["email"], "workout_type": "Crossfit", "details": {"desc": "Training for a crossfit competition"}, "date": datetime(2025, 5, 13, 14, 0)},
    {"_id": ObjectId(), "user": users[2]["email"], "workout_type": "Running Training", "details": {"desc": "Training for a marathon"}, "date": datetime(2025, 5, 13, 15, 0)},
    {"_id": ObjectId(), "user": users[3]["email"], "workout_type": "Strength Training", "details": {"desc": "Training for strength"}, "date": datetime(2025, 5, 13, 16, 0)},
    {"_id": ObjectId(), "user": users[4]["email"], "workout_type": "Swimming Training", "details": {"desc": "Training for a swimming competition"}, "date": datetime(2025, 5, 13, 17, 0)},
]
db.workouts.insert_many(workouts)

print("Successfully populated the database with test data.")
