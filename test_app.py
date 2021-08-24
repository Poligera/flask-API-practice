import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'

    def test_get_recipes(self, api):
        res = api.get('/recipes')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_recipe(self, api):
        res = api.get('/recipes/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Test recipe 2'

    def test_get_recipes_error(self, api):
        res = api.get('/recipes/4')
        assert res.status == '400 BAD REQUEST'
        assert "recipe with id 4" in res.json['message']

    # def test_post_recipes(self, api):
    #     mock_data = json.dumps({
    #         "name":"Vegan GF Sugar Free Chocoolate Natillas",
    #         "url": "localhost",
    #         "ingredients": ["100 cacao powder", "2 mature sharon fuit"],
    #         "method": "Pureed the fruit and mix it well with the cacao powder"
    #     })
    #     mock_headers = {'Content-Type': 'applirecipeion/json'}
    #     res = api.post('/recipes', data=mock_data, headers=mock_headers)
    #     assert res.status == '201 OK'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']