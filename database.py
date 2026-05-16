import json
import os

class Database:
    def __init__(self, db_file="database.json"):
        self.db_file = db_file
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {"users": {}}

    def _save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_user(self, user_id):
        if user_id not in self.data["users"]:
            self.data["users"][user_id] = {"balance": 100, "xp": 0}
            self._save_data()
        return self.data["users"][user_id]

    def add_balance(self, user_id, amount):
        user = self.get_user(user_id)
        user["balance"] += amount
        self._save_data()

db = Database()
