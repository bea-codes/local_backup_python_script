#Code created by bea-codes on GitHub.
#Use it as you like :)

import os
import shutil
from datetime import date

current_date = date.today()
date_format =  current_date.strftime("%d_%B_%Y_Copy_")


def backupFile(
    source_file_path,
    destination_path=None
    ):
    
    final_file_name = date_format+os.path.split(source_file_path)[1]  

    if not source_file_path:
        print('Please write source file path!')
        exit()

    if destination_path == None or destination_path.isspace() or not destination_path:
        destination_path = source_file_path
    
    if destination_path:
        destination_path = os.path.join(destination_path,final_file_name)


    shutil.copy2(source_file_path, destination_path)
    print("Backup done!", final_file_name)





backupFile('Insert File path here', 'Insert backup File Destination here')


