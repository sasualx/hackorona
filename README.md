# hackorona

use virtualenv pls,

then run the following commands to set it up (you need to have python 3, virtual env and npm installed:

`virtualenv env`
`. env/bin/activate`
`pip3 install -r requirements.txt`
`npm install package.json`

then you need to run these 2 in parralel in a terminal:

`npm run watch`
`python manage.py runserver`
and then you can see your beautiful website at localhost:8000