import csv
def main1():
    try:
     f=open("Students.csv","w",newline="")
     cw=csv.writer(f)
     cw.writerow(['Roll_No','Student_name','Gender,Y/N'])
     cw.writerow(['0290001',"Agaba","Male","Y"])
     cw.writerow(['0290002',"Atwiine","Male","N"])
     cw.writerow(['0290003',"Asiimwe","Male","Y"])
     cw.writerow(['0290004',"Asasira","Female","N"])
     cw.writerow(['0290005',"Ahabwe","Female","Y"])
     cw.writerow(['0290006',"Ankunda","Female","N"])
    except OSError:
        print("Error in creating csv file")
    finally:
        f.close()
main1()
