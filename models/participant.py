from sqlalchemy.orm import validates
from .database import db
from datetime import date

class Participant(db.Model):
    """Represents a participant who an assessment relates to """

    id = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    assessments = db.relationship(
        'Assessment',
        back_populates='participant',
        cascade='all, delete-orphan'
    )

    @validates('id')
    def validate_id(self, key, value):
        if not value:
            raise ValueError('Participant ID is required.')
        if len(value) != 9:
            raise ValueError('Participant ID must be exactly 9 characters long.')
        return value

    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError('Participant name is required.')
        value = value.strip()
        if len(value) < 2:
            raise ValueError('Participant name must be at least 2 characters long.')
        if len(value) > 50:
            raise ValueError('Participant name must be 50 characters or less.')
        return value
    
    @validates('dob')
    def validate_dob(self, key, value):
        if not value:
            raise ValueError('Date of birth is required.')
        
        # Ensure value is a date object
        if not isinstance(value, date):
            raise ValueError('Invalid date format.')
        
        # Check if DOB is in the future
        if value > date.today():
            raise ValueError('Date of birth cannot be in the future.')
        
        # Calculate age and check if 18+
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        
        if age < 18:
            raise ValueError('Participant must be at least 18 years old.')
        
        return value

    def __repr__(self):
        return f'<Participant {self.id}: {self.name}>'
