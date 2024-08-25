from utils import start_server
from config import read_config

if __name__ == "__main__":
    config = read_config()
    start_server(config)
