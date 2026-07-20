import sys
try:    
    import get_usage
    import alert
    import report
except ModuleNotFoundError:
    print("Module psutil non installé")
    print("Veuillez installer psutil avec la commande :'pip install psutil'")
    sys.exit(1)

if __name__ == "__main__":

    current = get_usage.get_all()

    alert.check_all(current)

    report.generate_report(current)
