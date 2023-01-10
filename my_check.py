import json
from deepdiff import DeepDiff

file_results = open('results.json')
file_correct_results = open('correct_results.json')

results = json.load(file_results)
correct_results = json.load(file_correct_results)

diff = DeepDiff(correct_results, results, ignore_order=True)

total_errors = 0

try:
    for key, values in diff['values_changed'].items() :
        print ("in", key, ":")
        print("- correct:", values["old_value"])
        print("- detected:", values["new_value"])
        print("\n")
        total_errors+=1

except:
    print("results are 100% correct")

print("The number of detected errors is:", total_errors)

file_results.close()
file_correct_results.close()