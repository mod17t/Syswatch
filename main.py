import get_usage
import alert
import report

if __name__ == "__main__":

    #collecter les données
    current = get_usage.get_all()

    #generer une alert si il le faut 
    alert.check_all(current)

    #generer un rapport
    report.generate_report(current)
