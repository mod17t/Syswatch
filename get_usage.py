try:
    import psutil
except ModuleNotFoundError:
    print("Module psutil non installer")
    print("Veuillez installer psutils avec la commande :'pip install psutil'")

def get_cpu_usage():
    return psutil.cpu_percent(interval=2)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_ps_usage():
    gen = list(psutil.process_iter(['name', 'cpu_percent', 'memory_percent']))
    gen.sort(key = lambda x: (x.info["memory_percent"] or 0, x.info["cpu_percent"] or 0) , reverse= True)
    ps_infos = [ps.info for ps in gen[:5]]
    return ps_infos

def get_all():
    return {
        "cpu": get_cpu_usage(),
        "ram": get_ram_usage(),
        "ps": get_ps_usage()
    }
