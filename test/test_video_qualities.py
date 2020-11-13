"""Video Qualities tests"""

from random import randrange

from test.conftest import video_quality
from utilities.custom_exceptions import RequestError


def test_get_video_qualities():
    """Get all items, check that the response list is not empty"""

    video_qualities = video_quality.read_all()
    assert len(video_qualities) > 0


def test_create_video_quality():
    """Create an item, check it was created correctly"""

    name = f"Quality {randrange(0, 10000)}"
    actual_video_q_created = video_quality.create(name)

    exp_video_q = {
        "id": video_quality.current_id,
        "name": name,
        "abbr": "AbbrVideoTest",
        "position": 1,
        "default": False
    }

    assert actual_video_q_created == exp_video_q

    actual_video_q_get = video_quality.read(video_quality.current_id)
    assert actual_video_q_get == exp_video_q


def test_negative_verify_error_message():
    """Verify the error message if parameter missing"""
    name = "Test Name"
    abbr = ""

    actual_msg = ""
    exp_msg = "Validation failed: Abbr can't be blank"

    try:
        video_quality.create(name, abbr=abbr)
    except RequestError as err:
        actual_msg = err.message

    assert exp_msg in actual_msg

def test_update_video_quality():
    """Update the item, check it was updated correctly"""

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

    actual_video_q = video_quality.read(video_q_id)
    assert actual_video_q == exp_video_q


def test_delete_video_quality():
    """Delete the item, check it was deleted (not found)"""

    video_quality_id = video_quality.current_id
    video_quality.delete(video_quality_id)

    expected_video_quality = None
    try:
        expected_video_quality = video_quality.read(video_quality_id)
    except RequestError:
        # If the request failed - it means, that the item was deleted
        pass

    assert expected_video_quality is None, f"Video Quality {video_quality_id} was not deleted"
