from models import Episode, Guest, Appearance

def test_episode_relationships(db):
    episode = Episode(date="1/1/99", number=1)
    guest = Guest(name="Test Guest", occupation="Tester")

    appearance = Appearance(rating=4, episode=episode, guest=guest)

    db.session.add_all([episode, guest, appearance])
    db.session.commit()

    assert appearance in episode.appearances
    assert appearance in guest.appearances

def test_rating_validation(db):
    episode = Episode(date="1/2/99", number=2)
    guest = Guest(name="Another Guest", occupation="Actor")
    db.session.add_all([episode, guest])
    db.session.commit()

    # Success
    valid = Appearance(rating=5, episode_id=episode.id, guest_id=guest.id)
    db.session.add(valid)
    db.session.commit()

    # Failure
    try:
        invalid = Appearance(rating=10, episode_id=episode.id, guest_id=guest.id)
        db.session.add(invalid)
        db.session.commit()
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True
