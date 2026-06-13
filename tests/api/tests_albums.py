import pytest
import requests

from jsonschema import validate
from schemas.schema_albums import SCHEMA_ALBUMS

@pytest.mark.parametrize("id_albums", [1,2,3,4,5])
def test_albums_validate(id_albums):
    response = requests.get(f"https://jsonplaceholder.typicode.com/albums/{id_albums}")

    assert response.status_code == 200

    validate(instance=response.json(), schema=SCHEMA_ALBUMS)