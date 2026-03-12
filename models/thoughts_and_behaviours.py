from sqlalchemy import Enum
from sqlalchemy.orm import validates
from .database import db


class ThoughtsAndBehaviours(db.Model):
    """Represents answers to the thoughts and behaviours section of an assessment"""

    # A negative score indicates disagreement with the question 
    # means this is an area you struggle with
    negative_score_map = {
        'Strongly Disagree': 1,
        'Disagree': 2,
        'Neither': 5,
        'Agree': 8,
        'Strongly Agree': 13,
    }

    # a positive score indicates agreeing with the question
    # means this is an area you struggle with
    positive_score_map = {
        'Strongly Disagree': 13,
        'Disagree': 8,
        'Neither': 5,
        'Agree': 2,
        'Strongly Agree': 1,
    }

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

    def score(self):
        """Return the total score from all answered items."""

        # These questions score higher the more "positive" the participant is about the question
        positive_answers = [
            self.bounce_back,
            self.working_hard,
            self.feel_good,
            self.adaptable,
            self.easy_to_talk
        ]
        negative_answers = [
            self.consequences,
            self.feelings,
            self.emotional_problems
        ]
        
        positiveScore = sum(self.positive_score_map[a] for a in positive_answers if a in self.positive_score_map)
        negativeScore = sum(self.negative_score_map[a] for a in negative_answers if a in self.negative_score_map)

        return negativeScore + positiveScore

    def colour(self):
        score = self.score()
        if score < 10:
            return "badge-danger" 
        if score < 25:
            return "badge-warning"
        return "badge-success"
