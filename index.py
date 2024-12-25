import csv
import check
import fix
from colorama import Style , init , Fore

data = []

with open('check_list.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        
        id = row.get("id").split("-")[1]
        
        print(f"Processing item : {id}")
        
        check_func = getattr(check , f"check{id}")
        check_val = check_func()
        if(check_val == "done"):
            print("Check result: " + Fore.GREEN + check_val + Style.RESET_ALL )
        else:
            print("Check result: " + Fore.RED + check_val + Style.RESET_ALL )
        row["check_result"] = check_val
        
        fix_func = getattr(fix , f"fix{id}")
        fix_val = fix_func()
        if(fix_val == "done"):
            print("Fix result: " + Fore.GREEN + fix_val + Style.RESET_ALL )
        else:
            print("Fix result: " + Fore.RED + fix_val + Style.RESET_ALL )
        row["fix_result"] = fix_val
        
        data.append(row)
            
            

with open('results.csv', mode='w', newline='') as file:
    fieldnames = ["id","severity","title","description","iacontrols","ruleID","fixid","fixtext","checkid","checktext","check_result","fix_result"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    csv_writer.writerows(data)
        