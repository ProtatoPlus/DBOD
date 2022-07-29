import docker
client = docker.from_env()
def createbot(token, prefix, type):
    tok = "BOT_TOKEN=" + str(token)
    pref = "PREFIX=" + str(prefix)
    cfg = [tok, pref]
    client.containers.run(type, detach=True, environment=cfg)
