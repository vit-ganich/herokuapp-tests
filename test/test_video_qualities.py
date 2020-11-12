from random import randrange

from test.conftest import video_quality


def test_get_video_qualities():
    video_qualities = video_quality.get_all()
    assert len(video_qualities) > 0


def test_create_video_quality():
    name = f"Quality {randrange(0, 10000)}"
    actual_video_q_created = video_quality.create(name)
    video_q_id = actual_video_q_created["id"]

    exp_video_q = {
        "id": video_q_id,
        "name": name,
        "abbr": "AbbrVideoTest",
        "position": 1,
        "default": False
    }

    assert actual_video_q_created == exp_video_q

    actual_video_q_get = video_quality.get(video_q_id)
    assert actual_video_q_get == exp_video_q


def test_update_video_quality():
    name = f"New Video Quality {randrange(0, 10000)}"
    video_q_id = video_quality.current_id
    video_quality.update(video_q_id, name)

    exp_video_q = {
        "id": video_q_id,
        "name": name,
        "abbr": "NewAbbrVideoTest",
        "position": 20,
        "default": True
    }

    actual_video_q = video_quality.get(video_q_id)
    assert actual_video_q == exp_video_q


def test_delete_video_quality():
    video_quality_id = video_quality.current_id
    video_quality.delete(video_quality_id)

    expected_video_quality = None
    try:
        expected_video_quality = video_quality.get(video_quality_id)
    except ConnectionRefusedError:
        pass

    assert expected_video_quality is None, f"Video Quality {video_quality_id} was not deleted"
