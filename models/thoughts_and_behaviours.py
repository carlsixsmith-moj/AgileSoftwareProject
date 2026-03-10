from sqlalchemy import Enum
from sqlalchemy.orm import validates
from .database import db


class ThoughtsAndBehaviours(db.Model):
    """Represents answers to the thoughts and behaviours section of an assessment"""

    answer_enum = Enum(
        'Strongly Disagree',
        'Disagree',
        'Neither',
        'Agree',
        'Strongly Agree',
        name='likert_response'
    )

    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(
        db.Integer,
        db.ForeignKey('assessment.id'),
        nullable=False,
        unique=True
    )
    assessment = db.relationship('Assessment', back_populates='thoughts_and_behaviours')
    bounce_back = db.Column(answer_enum, nullable=True)
    consequences = db.Column(answer_enum, nullable=True)
    working_hard = db.Column(answer_enum, nullable=True)
    feel_good = db.Column(answer_enum, nullable=True)
    adaptable = db.Column(answer_enum, nullable=True)
    feelings = db.Column(answer_enum, nullable=True)
    emotional_problems = db.Column(answer_enum, nullable=True)
    easy_to_talk = db.Column(answer_enum, nullable=True)

    @validates(
        'bounce_back',
        'consequences',
        'working_hard',
        'feel_good',
        'adaptable',
        'feelings',
        'emotional_problems',
        'easy_to_talk'
    )
    def validate_likert(self, key, value):
        if value is None:
            return value
        if value not in self.answer_enum.enums:
            raise ValueError(f'Invalid response value. {key}')
        return value
    
