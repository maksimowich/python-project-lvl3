logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
            'style': '{'
        }
    },

    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'std_format'
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'log',
            'level': 'DEBUG',
            'formatter': 'std_format'
        }
    },

    'loggers': {
        'app_console_logger': {
            'level': 'ERROR',
            'handlers': ['console_handler']
        },

        'app_file_logger': {
            'level': 'DEBUG',
            'handlers': ['file_handler']
        }
    }

}
