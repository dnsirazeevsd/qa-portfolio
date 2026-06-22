import pytest
from jsonschema import validate
from schemas.schema_albums import SCHEMA_ALBUMS
from schemas.schema_users import SCHEMA_USERS

#Обьединенный тест с параметизацией(альбомы, пользаватели)
@pytest.mark.parametrize(
    "path, schema",
    [
        ("/users/1", SCHEMA_USERS),
        ("/albums/1", SCHEMA_ALBUMS)
    ]
)
def test_albums_users(logged_request, path, schema):
    response = logged_request(path)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)