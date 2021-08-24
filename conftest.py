import pytest
import app
from controllers import recipes

@pytest.fixture
def api(monkeypatch):
    test_cats = [
        {
            "id":1,
            "name":"Vegan GF Sugar Free Chocoolate Natillas",
            "url": "localhost",
            "ingredients": ["100% cacao powder", "2 mature sharon fuit"],
            "method": "Pureed the fruit and mix it well with the cacao powder"
        },
         {
            "id":2,
            "name":"Test recipe 2",
            "url": "ldasf",
            "ingredients": ["dsf", "2dfdfs"],
            "method": "zvasdfasdfsfadr"
        }
    ]
    monkeypatch.setattr(recipes, "recipes", test_cats)
    api = app.app.test_client()
    return api