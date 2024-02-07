from dataclasses import dataclass
from random import randint


@dataclass
class User:
    user_id: str
    top_score: int = 0


db = [
    User("AAA01", 135),
    User("BBB01", 50),
    User("CCC01", 188),
    User("DDD01", 109)
]


def get_user(user_id: str) -> User | None:
    for entry in db:
        if entry.user_id == user_id:
            return entry
    return None


def print_users_list():
    print("\n==============================================================\n")
    for entry in db:
        print(f"{entry.user_id}: {entry.top_score}")
    print("\n==============================================================\n")


while True:
    id_to_search = input("Enter your ID (Enter 'xxx' to exit): ")
    if id_to_search.lower() == "xxx":
        break
    user = get_user(id_to_search)
    if not user:
        db.append(User(user_id=id_to_search, top_score=0))
        print(f"New user {id_to_search} added!")
    else:
        random_score = randint(50, 200)
        if random_score > user.top_score:
            user.top_score = random_score
            print(f"New score for {id_to_search}: {random_score}")

    print_users_list()
