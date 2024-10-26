import time

# Configuration
MAX_FAILED_ATTEMPTS = 3
LOCKOUT_DURATION = 300  # in seconds (5 minutes)
users = {
    'user1': 'password123',
    'user2': 'securepass',
}

# User state tracking
failed_attempts = {}
lockout_time = {}

def login(username, password):
    current_time = time.time()

    # Check if the user is locked out
    if username in lockout_time:
        if current_time < lockout_time[username]:
            remaining_time = lockout_time[username] - current_time
            print(f"User '{username}' is locked out. Please try again in {remaining_time:.0f} seconds.")
            return

    # Check username and password
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        failed_attempts[username] = 0  # reset on successful login
        if username in lockout_time:
            del lockout_time[username]  # clear lockout time
    else:
        print("Invalid username or password.")
        if username not in failed_attempts:
            failed_attempts[username] = 0

        failed_attempts[username] += 1

        if failed_attempts[username] >= MAX_FAILED_ATTEMPTS:
            lockout_time[username] = current_time + LOCKOUT_DURATION
            print(f"User '{username}' has been locked out for {LOCKOUT_DURATION // 60} minutes.")

def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username, password)

if __name__ == "__main__":
    main()