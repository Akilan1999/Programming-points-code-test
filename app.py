# VERSION 1
#This code base is for the purpose of the programming competition and not yet designed for analysing code.
#please read the Configuration Docs : This is only preconfigured with python for now but can work for any programmning langauges.

from flask import Flask, request, jsonify
app = Flask(__name__)
import subprocess
import os
import json
from datetime import datetime
from shutil import copyfile


'''This method is used to post solution and any updates on exisisting posted files must be done Admin incharge of the server

----------------------------------FILE STRUCTURE FOR STORING PROBLEM TEST CASES------------------------------------------------
(need to manually add the directories : <problem_no>,<languages>,unit test file )

   /langauge_unit_test
     /<problem_no> ... n : Can have as many problems as possible . Naming must be (problem<no>)
      /<programming langauge>
        / <unit test file>

----------------------------------FILE STRUCTURE FOR STORING SOLUTION------------------------------------------------
(These are completely auto generated hence )

   /code_files
     /<username> :Determined from the post request
      /version<no>
        / <code_file> , points.json : Stored the solution file with the timestamp,total points from the unit test

---------------------------------MODIFYING FOR SUPPORTING MULTIPLE PROGRAMMING LAGUAGES------------------------------
(Because this is version 1 you need to add from else if statements in future versions you can just edit a file for
support of different langauges.
)

This is code taken from line 76:
elif file.content_type == "application/octet-stream":  (Detects that the file is a python file in our case [TO FIND YOUR FILE SUBMIT TYPE UNCOMMENT LINE 71])
     file.save(os.path.join('langauge_unit_test/problem'+problem_no+'/<LANGUAGE NAME>', file.filename))
     test_dir_file_path = os.path.join('langauge_unit_test/problem'+problem_no+'/<LANGUAGE NAME>', file.filename)
     test_path = 'langauge_unit_test/problem'+problem_no+'/<LANGUAGE NAME>/problem'+problem_no+'_test.py'

     (You would need to provide the bash command to run the test file and must only output the total score in this version).
     Ex: If your command is python3 test_path : each word must be represented as separate in the array as shown below.
     result = subprocess.run(['python3',test_path], stdout=subprocess.PIPE)

     points = result.stdout (The output total score is stores in this varaible)



'''

@app.route('/postsolution', methods = ['POST'])
def postsolution():
    #read problem_no and usernamefrom shutil import copyfile
    problem_no = request.form.get('problem_no')
    username = request.form.get('username')

    #gets file from post request
    try:
            file = request.files['file']
    except:
            file = None

    if file != None:

        version_counter = 0
        points = 0
        test_dir_file_path = ""

       #print(file.content_type)
       # temporary way for doing unit test hence required to add to if statement for more langauges
        if file.content_type == "text/x-java-source":
             print("java")

        elif file.content_type == "application/octet-stream":
             file.save(os.path.join('langauge_unit_test/problem'+problem_no+'/python', file.filename))
             test_dir_file_path = os.path.join('langauge_unit_test/problem'+problem_no+'/python', file.filename)
             test_path = 'langauge_unit_test/problem'+problem_no+'/python/problem'+problem_no+'_test.py'
             result = subprocess.run(['python3',test_path], stdout=subprocess.PIPE)
             points = result.stdout

        #Creates a directory for user or adds code to exsisting directory
        if os.path.isdir("code_files/"+username):

             if os.path.isdir('code_files/'+username+'/problem'+problem_no):
                    while os.path.isdir('code_files/'+username+'/problem'+problem_no+'/version_'+ str(version_counter)):
                            version_counter+=1
                    os.makedirs('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter))
                    copyfile(os.path.join(test_dir_file_path),os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter), file.filename))
                    #file.save(os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter), file.filename))

             else:
                    os.makedirs('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter))
                    #file.save(os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter), file.filename))
                    copyfile(os.path.join(test_dir_file_path),os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter), file.filename))

             file.save(os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter),'points.json'))

             #Removes file from the test directory
             os.remove(test_dir_file_path)

            #Add points and datetime stamp to file
             now = datetime.now()
             dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

             data = {'timestamp': dt_string ,'point': points.decode('utf-8')}

             print(data)

             data = json.dumps(data)

             with open(os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter),'points.json'), 'w') as outfile:
                    json.dump(data, outfile)

             #remove file from testing path

        else:
            os.makedirs('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter))
            copyfile(os.path.join(test_dir_file_path),os.path.join('code_files/'+username+'/problem'+problem_no+'/version_'+str(version_counter), file.filename))
        return points

    else:
        return points
