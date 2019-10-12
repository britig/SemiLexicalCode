import os
import logicchecker
import utility

if __name__ == "__main__":
    input_directory_uni = "/home/amit/Desktop/SemiLexicalExperimentsCycle Dataset/unicycle"
    input_directory_bi = "/home/amit/Desktop/SemiLexicalExperimentsCycle Dataset/bicycle"
    # logicchecker.check_unicycle(input_directory, 'un1.jpg')

'''for filename in os.listdir(input_directory):
    print(filename)
    if ".jpg" in filename:
        result = logicchecker.check_unicycle(input_directory,filename)
        print(result)
    break'''

# Spatial distance computation for unicycles
for filename in os.listdir(input_directory_uni):
    if ".jpg" in filename:
        print(filename)
        utility.compute_spatial_uni(input_directory_uni, filename)

'''# Spatial distance computation for bicycles
for filename in os.listdir(input_directory_bi):
    if ".jpeg" in filename:
        print(filename)
        utility.compute_spatial_bi(input_directory_bi, filename)'''
