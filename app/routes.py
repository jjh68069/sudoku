from app.main import hello


def setup_routes(app):
    app.add_url_rule("/", view_func=hello)
