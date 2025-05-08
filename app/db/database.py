import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Loads environment variables from an .env file
load_dotenv()

# Setting up login details
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Creating a connection to Supabase
def get_supabase_instance() -> Client:
    return create_client(url, key)

# if __name__ == "__main__":
#     try:
#         supabase = get_supabase_instance()
#         print("Connection successful.")
#     except Exception as e:
#         print(f"Connection failed {e}.")
