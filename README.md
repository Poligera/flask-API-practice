# Sweet Bliss App
## Flask API practice (LAP 4)

#### Sweet Bliss App is a backend REST API created with Python and Flask framework.

#### Creators - Polina Moore, Monika Segarra and Debrah Francis.

## Run app:

_NB: These instructions assume you have Pipenv installed within your current version of Python.
- clone the repo and cd into the folder
- `pipenv shell`
- `pipenv install --dev`
- Run dev server with `pipenv run dev`
- Run prod server with `pipenv run start`
- Run tests with `pipenv run test`
- Get coverage report with `pipenv run coverage`


### Available routes: \
`GET`, `POST`: `/recipes` \
`GET`: `/recipes/:id`\


### Functionality:
- Home page displays "Hello from Sweet Bliss App! :)" message
- Users can see a full list of stored recipes
- Users can find a particular recipe by ID
- Users can add a recipe using Hopscotch, Postman, Thunderclient or any other API testing tool
- Added data does not persist as it is stored in a Python file for now


### Future features

- Add database for data storage
- Add UI (React.js)
- Improve "separation of concerns" on the backend using Model
- Increase test coverage
- Dockerizing the app
- Deployment (Heroku or PythonAnywhere)

