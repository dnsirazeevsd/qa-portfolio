import pytest

#Общий тест на структуру posts[]
def test_scope(posts_client):
    resp = posts_client("/posts")
    data = resp.json()

    assert resp.status_code == 200
    assert isinstance(data, list)

    assert len(data) == 100

#Тест на наличие полей в структуре обьекта post
@pytest.mark.parametrize("field",
[
    "userId",
    "id",
    "title",
    "body"
])
def test_struct_post(first_post, field):

    assert field in first_post
