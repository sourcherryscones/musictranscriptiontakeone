from api.main import bp


@bp.route('/')
def index():
    return "HELLO WORLD FROM MAIN/ROUTES"

@bp.route('/test', methods=['GET'])
def test():
    return "<h1>stuff things test route WOO</h1>"
