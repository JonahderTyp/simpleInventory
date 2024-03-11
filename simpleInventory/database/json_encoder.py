from datetime import datetime, date
from json import JSONEncoder
from . import db


class DatabaseEncoder(JSONEncoder):
    """Wandelt Datenbank-Klassen in JSON um"""

    @classmethod
    def default(self, obj):
        """Rekursive Funktion, die das Objekt in JSON zurückgibt

        Args:
            obj (db.Model): SQLAlchemy-Objekt

        Returns:
            dict: JSON-kompatibles dictionary
        """
        if obj == None:
            return None
        elif isinstance(obj, db.Model):
            return {k: v for k,v in obj.__dict__.items() if k in obj.__table__.columns.keys()}
        elif isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, tuple):
            raise TypeError()
            return {'__tuple__': True, 'items': [self.default(e) for e in obj]}
        elif isinstance(obj, list):
            return [self.default(e) for e in obj]
        elif isinstance(obj, dict):
            return {key: self.default(value) for key, value in obj.items()}
        return JSONEncoder.default(self, obj)