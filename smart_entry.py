from array import array

try:
    import torch
    tensor_available = True
except ImportError:
    tensor_available = False

# ---------- CONFIG (TUPLE) ----------
CLUB_RULES = ("ID required", "No minors", "No outside food")

# ---------- STORAGE ----------
entered_users = set()      # SET
visitor_log = []          # LIST
age_array = array("i")    # ARRAY

# ---------- DATABASE ----------
user_db = {
    101: {"name": "Rahul", "age": 22},
    102: {"name": "Anjali", "age": 17},
    103: {"name": "Kiran", "age": 25},
    104: {"name": "Suresh", "age": 19},
    105: {"name": "subhan", "age": 19},
    106: {"name": "Surendra", "age": 19},
    107: {"name": "subham", "age": 19},
    108: {"name": "sujatha", "age": 19}

}

# ---------- ENTRY ----------
def process_entry(user_id):
    if user_id not in user_db:
        print("User not found.")
        return

    user = user_db[user_id]
    name, age = user["name"], user["age"]

    if age < 18:
        print(f"{name} denied (minor).")
        return

    if user_id in entered_users:
        print(f"{name} already inside.")
        return

    # ---- Tensor logic (real use) ----
    if tensor_available and len(age_array) > 0:
        age_tensor = torch.tensor(age_array.tolist(), dtype=torch.float32)
        avg_age = age_tensor.mean().item()

        if avg_age < 21:
            print(f"Re-entry blocked: Crowd too young (avg age {avg_age:.1f})")
            return

    # Allow entry
    entered_users.add(user_id)
    visitor_log.append(name)
    age_array.append(age)

    print(f"{name} allowed inside.")


# ---------- EXIT ----------
def process_exit(user_id):
    if user_id in entered_users:
        entered_users.remove(user_id)

        # remove their age once from array
        age = user_db[user_id]["age"]
        name=user_db[user_id]["name"]
        age_array.remove(age)

        print(f"User {user_id,name} exited.")
    else:
        print("User not inside.")


# ---------- TESTING ----------
if __name__ == "__main__":
    test_ids = [101, 102, 103, 104, 105, 106, 107, 108]

    for uid in test_ids:
        process_entry(uid)

    print("\nCurrent Visitors:", {uid:user_db[uid]["name"] for uid in entered_users})

    for uid in [101, 103, 105]:
        process_exit(uid)

    print("\nVisitors after exits:", {uid: user_db[uid]["name"] for uid in entered_users})