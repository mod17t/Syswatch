from datetime import datetime
import os 

def generate_report(current):
    # la variable now va permettre de recuperer la date actuelle au format year-month-day_hours-minutes-seconds 
    now = datetime.now()
    #creations du repertoire reports s'il n'existe pas encore
    os.makedirs("reports", exist_ok=True)
    #creation du fichier de rapports
    with open(f"reports/report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt", "w", encoding="utf-8") as f:
        f.write(f"Rapport généré le {now.strftime('%d/%m/%Y')} à {now.strftime('%H:%M:%S')} \n\n")
        f.write(f"La consommation du CPU est : {current['cpu']}  \n")
        f.write(f"La consommation de la RAM est : {current['ram']} \n")
        f.write(f"Les processus qui consomment le plus sont : \n")
        for ps in current["ps"]:
            f.write(f"  nom : {ps['name']} \n")
            f.write(f"  consommation RAM : {ps['memory_percent']:.2f}% \n")
            f.write(f"  Consommation CPU : {ps['cpu_percent']:.2f}% \n")
        
