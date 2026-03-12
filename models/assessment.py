from sqlalchemy.orm import validates
from .database import db
from datetime import date
class Assessment(db.Model):
    """Represents an assessment that has been carried out against a participant, when it occured"""
    id = db.Column(db.Integer, primary_key=True)
    date_recorded = db.Column(db.Date, nullable=False)
    participant_id = db.Column(db.String(9), db.ForeignKey('participant.id'), nullable=False)
    participant = db.relationship('Participant', back_populates='assessments')
    thoughts_and_behaviours = db.relationship(
        'ThoughtsAndBehaviours',
        back_populates='assessment',
        uselist=False,
        cascade='all, delete-orphan'
    )

    @validates('participant_id')
    def validate_id(self, key, value):
        if not value:
            raise ValueError('Participant ID is required.')
        if len(value) != 9:
            raise ValueError('Participant ID must be exactly 9 characters long.')
        
        return value
    
    @validates('date_recorded')
    def validate_date_recorded(self, key, value):
        if not value:
            raise ValueError('Date Recorded is required')
        
        # Ensure value is a date object
        if not isinstance(value, date):
            raise ValueError('Invalid date format.')

        if value > date.today():
            raise ValueError('Record Date cannot be in the future')
        
        return value;