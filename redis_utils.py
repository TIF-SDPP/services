import redis
import json
from dotenv import load_dotenv
import os 


class RedisUtils:
    load_dotenv()
    redis_host = os.getenv("REDIS_HOST")
    redis_password = os.getenv("REDIS_PASSWORD")
    def __init__(self, host=redis_host, port=6379, db=0, password=redis_password):
        """Initialize Redis connection with security."""
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password)

    def post_message(self, message, list_key='blockchain'):
        """Serialize and add a message to the beginning of a Redis list."""
        message_json = json.dumps(message)
        self.redis_client.lpush(list_key, message_json)

    def get_recent_messages(self, list_key='blockchain', count=10):
        """Retrieve the last 'count' messages from a Redis list."""
        messages_json = self.redis_client.lrange(list_key, 0, count - 1)
        return [json.loads(msg) for msg in messages_json]

    def get_latest_element(self, list_key='blockchain'):
        """Retrieve the latest element from a Redis list."""
        latest_element_json = self.redis_client.lindex(list_key, 0)
        if latest_element_json:
            return json.loads(latest_element_json)
        return None  # Return None if the list is empty
    
    def exists_id(self, id, list_key='blockchain'):
        """Check if an ID exists in the list."""
        messages_json = self.redis_client.lrange(list_key, 0, -1)  # Retrieve all messages
        for msg_json in messages_json:
            msg = json.loads(msg_json)
            if 'id' in msg and msg['id'] == id:
                return True
        return False
# The module can be used after import by creating an instance of RedisUtils