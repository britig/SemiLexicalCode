import os
import logicchecker
import testimg as tg
import utility

if __name__ == "__main__":
    tg.run_yolo()
    input_directory = "../testimg/modified"
    # logicchecker.check_unicycle(input_directory, 'un1.jpg')

'''for filename in os.listdir(input_directory):
    print(filename)
    if ".jpg" in filename:
        result = logicchecker.check_unicycle(input_directory,filename)
        print(result)
    break'''

# Spatial distance computation for unicycles
for filename in os.listdir(input_directory):
    if ".jpg" in filename:
        print(filename)
        result = utility.compute_spatial_uni(input_directory, filename)
        print("uni"+str(result))

# Spatial distance computation for bicycles
for filename in os.listdir(input_directory):
    if ".jpg" in filename:
        print(filename)
        result = utility.compute_spatial_bi(input_directory, filename)
        print("bi"+str(result))
