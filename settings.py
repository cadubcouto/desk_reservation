import environ

env = environ.Env()
environ.Env.read_env()

DATABASE_IP_APP = env("DATABASE_IP_APP")
USER_DATABASE_APP = env("USER_DATABASE_APP")
POSTGRES = env("POSTGRES")

