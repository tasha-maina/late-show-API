from models import Episode, Guest, Appearance, db

def seed(db):
    e1 = Episode(date="1/11/99", number=1)
    e2 = Episode(date="1/12/99", number=2)

    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="comedian")

    a1 = Appearance(rating=4, episode=e1, guest=g1)

    db.session.add_all([e1, e2, g1, g2, a1])
    db.session.commit()


def test_get_episodes(client, db):
    seed(db)
    response = client.get("/episodes")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_get_episode_by_id(client, db):
    seed(db)
    response = client.get("/episodes/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1


def test_get_episode_not_found(client, db):
    response = client.get("/episodes/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Episode not found"


def test_delete_episode(client, db):
    seed(db)
    response = client.delete("/episodes/1")
    assert response.status_code == 204


def test_get_guests(client, db):
    seed(db)
    response = client.get("/guests")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_post_appearance(client, db):
    seed(db)
    body = {
        "rating": 5,
        "episode_id": 1,
        "guest_id": 2
    }
    response = client.post("/appearances", json=body)
    assert response.status_code == 201
    assert response.get_json()["rating"] == 5
