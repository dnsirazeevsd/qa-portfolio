import pytest
from jsonschema import validate
from schemas.schema_albums import SCHEMA_ALBUMS

@pytest.mark.parametrize("id_albums", [1, 2, 3, 4, 5])
def test_albums_validate(api_client, id_albums):
    response = api_client(f"/albums/{id_albums}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=SCHEMA_ALBUMS)