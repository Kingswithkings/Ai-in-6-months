import json
from collections import Counter
from typing import List, Tuple

def get_top_users(filepath: str, top_n: int = 3) -> List[Tuple[str, int]]:
    """
    Reads a JSON file containing chat messages, counts messages per user, and returns the top N users by message count.
    
    The expected JSON format is a list of objects like:
    [{"user": "Username", "message": "Content"}, ...]
    
    Args:
        filepath: The path to the JSON file.
        top_n: The number of the top users to return (default is 3).
         
        Returns:
         A list of tuples [(username, message_count), ...]
        """
    try:
        # 1. Read the JSON file
        with open(filepath, 'r') as f:
            messages = json.load(f)

        # 2. Extract all usernames
        usernames = [msg.get('user') for msg in messages if msg.get('user')]

        # 3. Count occurences of each username
        user_counts = Counter(usernames)

        # 4. Get the top N most common users
        top_users = user_counts.most_common(top_n)

        return top_users
    
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'. Check file format")
        return []
    except Exception as e:
        print(f"An unexpected error occcured: {e}")
        return []
    
if __name__ == "__main__":
    json_filepath = 'chat_messages.json'

    print(f"Analyzing chat data from {json_filepath}...")
    top_3 = get_top_users(json_filepath, top_n=3)

    if top_3:
        print("\n--- Top 3 Users by Message Count ---")
        for rank, (user, count) in enumerate(top_3, 1):
            print(f"Rank {rank}: {user} ({count} messages)")
    else:
        print("Analysis could not be completed.")