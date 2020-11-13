"""Audio Qualities tests"""

from random import randrange

from test.conftest import audio_quality
from utilities.custom_exceptions import RequestError


def test_get_audio_qualities():
    """Get all items, check that the response list is not empty"""

    video_qualities = audio_quality.read_all()
    assert len(video_qualities) > 0


def test_create_audio_quality():
    """Create an item, check it was created correctly"""

    name = f"Quality {randrange(0, 10000)}"
    actual_audio_q_created = audio_quality.create(name)

    exp_audio_q = {
        "id": audio_quality.current_id,
        "name": name,
        "abbr": "AbbrAudioTest",
        "position": 1,
        "default": False
    }

    assert actual_audio_q_created == exp_audio_q

    actual_audio_q_get = audio_quality.read(audio_quality.current_id)
    assert actual_audio_q_get == exp_audio_q


def test_update_audio_quality():
    """Update the item, check it was updated correctly"""

    name = f"New Quality {randrange(0, 10000)}"
    audio_q_id = audio_quality.current_id
    audio_quality.update(audio_q_id, name)

    exp_audio_q = {
        "id": audio_q_id,
        "name": name,
        "abbr": "NewAbbrAudioTest",
        "position": 20,
        "default": True
    }

    actual_audio_q = audio_quality.read(audio_q_id)
    assert actual_audio_q == exp_audio_q


def test_delete_audio_quality():
    """Delete the item, check it was deleted (not found)"""

    audio_quality_id = audio_quality.current_id
    audio_quality.delete(audio_quality_id)

    expected_audio_quality = None
    try:
        expected_audio_quality = audio_quality.read(audio_quality_id)
    except RequestError:
        # If the request failed - it means, that the item was deleted
        pass

    assert expected_audio_quality is None, f"Audio Quality {audio_quality_id} was not deleted"
