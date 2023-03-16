import os


folder = r"C:\Users\Public\Documents\CHINÁ\Chin\\"  #"C:\Users\DRONES\Desktop\ChinaPPK\OUTPUT\\" 
count = 137
# Iterate through the folder
for file in os.listdir(folder):
    
    # construct current name using file name and path
    old_name = os.path.join(folder, file)
    # get file name without extension
    only_name = os.path.splitext(file)[0]

    if (only_name.startswith("China2_Flight_02")):
        # Renaming the file name
        #only_name = only_name[:5] + "" + only_name[-16:]
        only_name = only_name[:19].replace("China2", "China") + str(count)   
        count += 1

        # Adding the new name with extension
        new_base = only_name + ".jpg"
        # construct full file path
        new_name = os.path.join(folder, new_base)

        # Renaming the file
        os.rename(old_name, new_name)

# verify the result
res = os.listdir(folder)
print(res)

