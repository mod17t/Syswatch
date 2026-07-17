import sys
try:    
    import get_usage
    import alert
    import report
except ModuleNotFoundError:
    print("Module psutil non installer")
    print("Veuillez installer psutils avec la commande :'pip install psutil'")
    sys.exit()

if __name__ == "__main__":

    #collecter les données
    current = get_usage.get_all()

    #generer une alert si il le faut 
    alert.check_all(current)

    #generer un rapport
    report.generate_report(current)
