from .db import SessionLocal, RequestLog

class MonitorDB:
    """Database handler for monitoring requests."""

    def __init__(self):
        self.db = SessionLocal()

    def log_request(self, endpoint, provider, user_email, user_id):
        """Log a request into the monitoring database."""
        new_log = RequestLog(
            endpoint=endpoint,
            provider=provider,
            user_email=user_email,
            user_id=user_id
        )
        self.db.add(new_log)
        self.db.commit()

    def get_requests(self):
        """Retrieve all logged requests."""
        return self.db.query(RequestLog).order_by(RequestLog.timestamp.desc()).all()

# Instantiate the database handler
monitor_db = MonitorDB()
