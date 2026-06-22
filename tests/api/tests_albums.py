import pytest
from jsonschema import validate
from schemas.schema_albums import SCHEMA_ALBUMS

#Тест с 5 параметрами - для проверки коллекции id альбомов
@pytest.mark.parametrize("id_albums", [1, 2, 3, 4, 5])
def test_albums_validate(logger_request, id_albums):
    response = logger_request(f"/albums/{id_albums}", method="GET")
    assert response.status_code == 200
    validate(instance=response.json(), schema=SCHEMA_ALBUMS)


