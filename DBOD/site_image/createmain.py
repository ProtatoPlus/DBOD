import docker
client = docker.from_env()
def createbot(token, prefix):
    tok = "BOT_TOKEN=" + str(token)
    pref = "PREFIX=" + str(prefix)
    cfg = [tok, pref]
    client.containers.run("dbod_image", detach=True, environment=cfg)
