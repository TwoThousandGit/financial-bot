from utils.db_api.sqlite import Database

db = Database()

def test():
        db.create_table_users()
        users = db.select_all_users()
        print(f"До добавления пользователей: {users}")
        db.add_user(1, "One")
        db.add_user(2, "Two")
        db.add_user(3, "Tree")
        users = db.select_all_users()
        print(f"После добавления пользователей: {users}")
        user = db.select_user(Name="Tree", id=3)
        print(f"Получил пользователя {user}")

test()
