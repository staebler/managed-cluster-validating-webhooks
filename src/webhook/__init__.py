from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from webhook import group_validation
app.register_blueprint(group_validation.bp)

from webhook import subscription_validation
app.register_blueprint(subscription_validation.bp)

from webhook import namespace_validation
app.register_blueprint(namespace_validation.bp)

from webhook import regular_user_validation
app.register_blueprint(regular_user_validation.bp)

from webhook import metrics
app.register_blueprint(metrics.bp)
