from xians import api
from xians.controllers import city, user, favorite

api.add_resource(city.City, '/cities/<int:_id>', endpoint='city_id')
api.add_resource(city.City, '/cities/<string:name>', endpoint='city_name')


api.add_resource(user.User, '/users')


api.add_resource(favorite.Favorites, '/favorites')
api.add_resource(favorite.Favorite, '/favorite/<int:city_id>')
