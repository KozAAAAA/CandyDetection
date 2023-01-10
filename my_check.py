import json
from deepdiff import DeepDiff

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def my_check():
    file_results = open('results.json')
    file_correct_results = open('correct_results.json')
    
    results = json.load(file_results)
    correct_results = json.load(file_correct_results)
    
    diff = DeepDiff(correct_results, results, ignore_order=True)

    total_errors = 0

    try:
        for key, values in diff['values_changed'].items() :
            print (color.BOLD + color.CYAN + "@ In " + str(key) + ":" + color.END + color.END)
            print(color.GREEN + "correct: " + color.END + str(values["old_value"]))
            print(color.RED + "detected:" + color.END + str(values["new_value"]) + "\n")
            total_errors+=1

    except:
        print("results are 100% correct")

    print(color.BOLD + color.RED + "@ The number of detected errors is: " + color.END + color.END + str(total_errors))

    file_results.close()
    file_correct_results.close()

my_check()