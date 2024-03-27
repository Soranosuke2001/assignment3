import yaml, logging.config, logging


def read_app_config():
    with open('./config/app_conf.yml', 'r') as file:
        app_config = yaml.safe_load(file.read())

    return app_config


def get_mysql_config():
    app_config = read_app_config()

    hostname = app_config['mysql']['url']
    user = app_config['mysql']['user']
    password = app_config['mysql']['password']
    port = app_config['mysql']['port']
    db = app_config['mysql']['db']

    return hostname, user, password, port, db


def get_sqlite_config():
    app_config = read_app_config()

    filename = app_config['datastore']['filename']
    seconds = app_config['scheduler']['period_sec']
    url = app_config['eventstore']['url']

    return filename, seconds, url


def get_flask_config():
    app_config = read_app_config()

    host = app_config["flask"]["host"]
    port = app_config["flask"]["port"]

    return host, port


def read_log_config():
    with open('./config/log_conf.yml', 'r') as file:
        log_config = yaml.safe_load(file.read())
        logging.config.dictConfig(log_config)

    logger = logging.getLogger('basicLogger')

    return logger

