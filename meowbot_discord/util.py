from functools import lru_cache

import redis
import yaml


YAML_CONF_PATH = "config/config.yaml"
REDIS_URL = "redis://redis:6379/0"


@lru_cache(maxsize=1)
def get_config():
    with open(YAML_CONF_PATH, "r") as fp:
        return yaml.safe_load(fp)


def get_bot_token():
    return get_config()["bot_token"]


def get_cat_api_key():
    return get_config()["cat_api_key"]


def get_default_guild_id():
    return get_config()["default_guild_id"]


@lru_cache(maxsize=1)
def get_redis():
    return redis.Redis.from_url(REDIS_URL)
