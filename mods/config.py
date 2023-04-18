from configparser import ConfigParser

config = ConfigParser()
config.read("conf.ini")

model = {
    'eye': {
        'path': config.get('eyeModel', 'path'),
        "resolution": config.getint('eyeModel', 'resolution'),
        "weight": config.getint('eyeModel', 'weight'),
        "time": config.getint('eyeModel', 'time'),
        "blinkCount": config.getint('eyeModel', 'blinkCount'),
        "faultRatio": config.getfloat('eyeModel', 'faultRatio'),
        "window": config.getint('eyeModel', 'window')
    },
    'mouth': {
        'path': config.get('mouthModel', 'path'),
        "resolution": config.getint('mouthModel', 'resolution'),
        "weight": config.getint('mouthModel', 'weight'),
        "time": config.getint('mouthModel', 'time'),
        "faultRatio": config.getfloat('mouthModel', 'faultRatio')
    }
}

basic = {
    'fps': config.getint('basic', 'fps'),
    'maxWarn': config.getint('basic','maxWarn'),
    'reduceTime': config.getint('basic','reduceTime')
}