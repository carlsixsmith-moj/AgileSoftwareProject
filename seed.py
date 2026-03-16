import sys
import os
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import db, Participant, Assessment, User


def seed_database():
    """Run within an active app context to create tables and seed initial data."""
    db.create_all()
    print('Created database schema')

    # Seed default users
    if User.query.first() is None:
        admin = User(username='admin', role='admin')
        admin.set_password('admin')

        user = User(username='user', role='user')
        user.set_password('user')

        users = [
            admin,
            user
        ]

        db.session.add_all( users )
        db.session.commit()
        
        print("\nUsers created")
        for u in users:
            print(f"    [{u.username}] {u.role}")
    else:
        print('\nUsers already exist, skipping user seeding.')

    # Seed default participants
    if Participant.query.first() is None:
        default_dob = date(1990, 1, 1)
        participants = [
            Participant(id="1CFG1109X", name="Barry Stone", dob=default_dob),
            Participant(id="1CFG1333S", name="Peter Allen", dob=default_dob),
            Participant(id="1CFG1553F", name="VICTOR JORDAN", dob=default_dob),
            Participant(id="1CFG1626P", name="BRUCE CURRY", dob=default_dob),
            Participant(id="1CFG2457U", name="BRUCE WAYNE", dob=default_dob),
            Participant(id="1CFG2622V", name="DINAH JORDAN", dob=default_dob),
            Participant(id="1CFG2883L", name="OLIVER PRINCE", dob=default_dob),
            Participant(id="1CFG4261Y", name="DIANA WAYNE", dob=default_dob),
            Participant(id="1CFG4595K", name="CLARK KENT", dob=default_dob),
            Participant(id="1CFG4867Q", name="OLIVER JORDAN", dob=default_dob),
            Participant(id="1CFG4936J", name="VICTOR JORDAN", dob=default_dob),
            Participant(id="1CFG5131C", name="BARRY ALLEN", dob=default_dob),
            Participant(id="1CFG5298O", name="VICTOR JORDAN", dob=default_dob),
            Participant(id="1CFG5437L", name="HAL PARKER", dob=default_dob),
            Participant(id="1CFG5469L", name="PETER QUEEN", dob=default_dob),
            Participant(id="1CFG5854G", name="DINAH QUEEN", dob=default_dob),
            Participant(id="1CFG6059P", name="Oliver Kent", dob=default_dob),
            Participant(id="1CFG6390M", name="ARTHUR LANCE", dob=default_dob),
            Participant(id="1CFG7256O", name="BARRY PARKER", dob=default_dob),
            Participant(id="1CFG7276C", name="OLIVER PRINCE", dob=default_dob),
            Participant(id="1CFG8236D", name="BRUCE ALLEN", dob=default_dob),
            Participant(id="1CFG8391O", name="HAL KENT", dob=default_dob),
            Participant(id="1CFG8432I", name="HAL CURRY", dob=default_dob),
            Participant(id="1CFG8516T", name="DINAH KENT", dob=default_dob),
            Participant(id="1CFG9326Y", name="BRUCE KENT", dob=default_dob),
            Participant(id="1CFG9475S", name="VICTOR JORDAN", dob=default_dob),
            Participant(id="1CFG9798U", name="Hal Queen", dob=default_dob),
            Participant(id="1CFG9960M", name="BRUCE LANCE", dob=default_dob)
        ]
        db.session.add_all(participants)
        db.session.commit()

        print("\nParticipants created")
        for p in participants:
            print(f"    [{p.id}] {p.name}")
    else:
        print("\nParticipants already exist, skipping participant seeding.")


if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed_database()
