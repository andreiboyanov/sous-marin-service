from sous_marin.core.config import settings


def test_project_name_not_empty():
    assert len(settings.project_name) > 0


def test_api_v1_path_not_empty():
    assert len(settings.api_v1_path) > 0
