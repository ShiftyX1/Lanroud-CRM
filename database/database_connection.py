from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import ConfigurationError
from fastapi import FastAPI



class Database:
    def __init__(self, db_url: str = None, host: str = None, port: str = None, user: str = None, password: str = None, database: str = None, engine: str = None):
        """
        Setting up and creating Database connection config
        """
        self.host: str = host
        self.port: str = port
        self.user: str = user
        self.password: str = password
        self.database: str = database
        self.engine: str = engine
        self.db_url: str = db_url
        config_default = {
               'connections': {
                    'default': {
                        'engine': self.engine,
                        'credentials': {
                            'host': self.host,
                            'port': self.port,
                            'user': self.user,
                            'password': self.password,
                            'database': self.database,
                        }
                    },
                },
                'apps': {
                    'models': {
                        "models": ["aerich.models"],
                        'default_connection': 'default',
                    }
                }
            }
        config_url =  {
            "connections": 
                {"default": self.db_url},
            "apps": {
                "models": {
                    "models": ["aerich.models"],
                    "default_connection": "default",
                    },
                },
            }
        if self.db_url == None:
            self.config: str = config_default
        else:
            self.config: str = config_url

    def get_config(self) -> str:
        """
        Return database final TORTOISE config
        """
        return self.config
    
    def connect_database(self, app: FastAPI) -> None:
        try:
            register_tortoise(app=app, config=self.config)
            print(f"Succes connection to Database {self.database} on {self.host}:{self.port}")
        except ConfigurationError as e:
            print(f"Configuration error occured during connecting to Database {self.database} on {self.host}:{self.port}!")
