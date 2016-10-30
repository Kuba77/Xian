from xians import api
from xians.controllers import city, user, favorite

api.add_resource(city.City, '/city/<int:_id>', endpoint='city_id')
api.add_resource(city.City, '/city/<string:name>', endpoint='city_name')
api.add_resource(city.CityDetails, '/city/<int:_id>/details')

api.add_resource(user.UserSignup, '/signup')


api.add_resource(favorite.Favorite, '/favorite/<int:city_id>')
