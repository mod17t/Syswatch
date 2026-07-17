import config

def check_all(current):

    if current["cpu"] >= config.ALERT_THRESHOLDS["cpu"]:
        print("Alerte la consomation du cpu depasse la limite")

    if current["ram"] >= config.ALERT_THRESHOLDS["ram"]:
        print("Alerte la consomation de la ram depasse la limite")
    