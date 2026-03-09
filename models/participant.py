from .database import db

class Participant(db.Model):
    """Represents a participant who an assessment relates to """

    id = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    assessments = db.relationship(
        'Assessment',
        back_populates='participant',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Participant {self.id}: {self.name}>'
