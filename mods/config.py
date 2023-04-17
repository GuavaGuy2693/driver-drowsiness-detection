from configparser import ConfigParser

config = ConfigParser()
config.read("conf.ini")

model = {
    'eye': {
        'path': config.get('eyeModel', 'path'),
        "resolution": config.getint('eyeModel', 'resolution'),
        "warn": config.getint('eyeModel', 'warn'),
        "time": config.getint('eyeModel', 'time'),
        "faultTimeRatio": config.getfloat('eyeModel', 'faultTimeRatio')
    },
    'mouth': {
        'path': config.get('mouthModel', 'path'),
        "resolution": config.getint('mouthModel', 'resolution'),
        "warn": config.getint('mouthModel', 'warn'),
        "time": config.getint('mouthModel', 'time'),
        "faultTimeRatio": config.getfloat('mouthModel', 'faultTimeRatio')
    }
}

basic = {
    'fps': config.getint('basic', 'fps'),
    'maxWarn': config.getint('basic','maxWarn'),
    'reduceTime': config.getint('basic','reduceTime')
}