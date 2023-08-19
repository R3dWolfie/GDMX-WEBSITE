from flask_bcrypt import Bcrypt
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    # General Website details
    id = db.Column(db.BigInteger, primary_key=True)
    siteUsername = db.Column(db.String(512), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)  # Rename to password_hash
    gameUsername = db.Column(db.String(512), unique=False, nullable=False)
    email = db.Column(db.String(512), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    # Robtop IDs
    playerId = db.Column(db.BigInteger, unique=True, nullable=False)
    accountId = db.Column(db.BigInteger, unique=True, nullable=False)

    # Patreon sub Tier
    tier = db.Column(db.Integer, unique=False, nullable=False)

    # Settings
    port = db.Column(db.String, unique=False, nullable=False)
    serverIp = db.Column(db.String, unique=True, nullable=False)
    renderCustomIcons = db.Column(db.String, unique=False, nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.siteUsername}>"