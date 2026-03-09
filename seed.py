import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, Participant, Assessment

with app.app_context():
    db.create_all()
    print('Created database schema')

    if Participant.query.first():
        print("\nParticipants already exist, skipping seeding.")
    else:
        participants = [
            Participant(id="1CFG1109X", name="Barry Stone"),
            Participant(id="1CFG1333S", name="Peter Allen"),
            Participant(id="1CFG1553F", name="VICTOR JORDAN"),
            Participant(id="1CFG1626P", name="BRUCE CURRY"),
            Participant(id="1CFG2457U", name="BRUCE WAYNE"),
            Participant(id="1CFG2622V", name="DINAH JORDAN"),
            Participant(id="1CFG2883L", name="OLIVER PRINCE"),
            Participant(id="1CFG4261Y", name="DIANA WAYNE"),
            Participant(id="1CFG4595K", name="CLARK KENT"),
            Participant(id="1CFG4867Q", name="OLIVER JORDAN"),
            Participant(id="1CFG4936J", name="VICTOR JORDAN"),
            Participant(id="1CFG5131C", name="BARRY ALLEN"),
            Participant(id="1CFG5298O", name="VICTOR JORDAN"),
            Participant(id="1CFG5437L", name="HAL PARKER"),
            Participant(id="1CFG5469L", name="PETER QUEEN"),
            Participant(id="1CFG5854G", name="DINAH QUEEN"),
            Participant(id="1CFG6059P", name="Oliver Kent"),
            Participant(id="1CFG6390M", name="ARTHUR LANCE"),
            Participant(id="1CFG7256O", name="BARRY PARKER"),
            Participant(id="1CFG7276C", name="OLIVER PRINCE"),
            Participant(id="1CFG8236D", name="BRUCE ALLEN"),
            Participant(id="1CFG8391O", name="HAL KENT"),
            Participant(id="1CFG8432I", name="HAL CURRY"),
            Participant(id="1CFG8516T", name="DINAH KENT"),
            Participant(id="1CFG9326Y", name="BRUCE KENT"),
            Participant(id="1CFG9475S", name="VICTOR JORDAN"),
            Participant(id="1CFG9798U", name="Hal Queen"),
            Participant(id="1CFG9960M", name="BRUCE LANCE")
        ]
        db.session.add_all(participants)
        db.session.commit()

        print("\nParticipants created")
        for p in participants:
            print(f"    [{p.id}] {p.name}")