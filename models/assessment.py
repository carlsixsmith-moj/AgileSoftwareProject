from .database import db


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