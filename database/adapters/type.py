from sqlalchemy import String
from uuid import uuid4
UUID = String(36)

def generate_uuid():
    return str(uuid4())