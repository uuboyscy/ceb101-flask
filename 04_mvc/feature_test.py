from flask import Blueprint

feature_test = Blueprint('feature_test', __name__)

@feature_test.route('/feature_test')
def feature_test_controller():
    return 'Feature controller'
