import yaml, logging.config, logging


def read_app_config():
    with open('./config/app_conf.yml', 'r') as file:
        app_config = yaml.safe_load(file.read())

    return app_config


def get_urls():
    app_config = read_app_config()

    return app_config['newGunStat']['url'], app_config['newItemTransaction']['url']


def get_kafka_config():
    app_config = read_app_config()

    return app_config['events']['hostname'], app_config['events']['port'], app_config['events']['topic']


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
