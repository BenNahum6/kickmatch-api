import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Loads environment variables from an .env file
load_dotenv()

class DatabaseSupabase:
    """
    Singleton class managing the connection to the Supabase database.

    Ensures only one client instance is created and reused across the application.
    """

    _instance = None

    def __new__(cls):
        """
        Creates or returns the singleton instance of Database_supabase.

        param cls: The class itself.
        :return: The singleton instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_KEY")
            cls._instance._client = create_client(url, key)
            print(f'Database_supabase instance created: {cls._instance._client}')
        return cls._instance

    @property
    def client(self) -> Client:
        """
        :return: The Supabase Client object.
        """
        return self._client