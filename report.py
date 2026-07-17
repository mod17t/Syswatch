
def generate_report(current):
    with open("report.txt", "w") as f:
        f.write(f"La consommation du CPU est : {current["cpu"]}  \n")
        f.write(f"La consommation de la RAM est : {current["ram"]} \n")
        f.write(f"Les processus qui consomment le plus sont : \n")
        for ps in current["ps"]:
            f.write(f"  nom : {ps["name"]} \n")
            f.write(f"  consommation RAM : {ps["memory_percent"]:.2f}% \n")
            f.write(f"  Consommation CPU : {ps["cpu_percent"]:.2f}% \n")
        
