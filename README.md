FILE STRUCTURE:
          fapi--->
                  project--->
                             pro --->
                                     centre.py
                                     crud.py
                                     data.csv
                                     database.py
                                     json_demo.py
                                     json_path
                                     load.py
                                     model.py
                                     operations.py
                                     schemas.py
                                     test_crud.py
                                 
                                 

DESCRIPTION:
--------------

MAIN FILES:
         model.py --- create a database tables(pincode and geojson) and connection.
         schemas.py --- create a model attribute or columns.
         crud.py --- resolve queries with reusable functions to interact with the data in the database.
                      CRUD comes from: Create, Read, Update, and Delete.
         operations.py --- create a GET and POST method. 
         test_crud.py --- It is used for testing pusrpose using pytest and make testcases.
         load.py --- load the CSV data into database of both the task(1st and 3rd)

ADDITIONAL FILES:
         centre.py --- gives the centre of all the boundry latitudes and longitudes of specific area.
         data.csv --- mapping B/W pincode,address,city,latitude and longitude
                      (https://github.com/sanand0/pincode/blob/master/data/IN.csv)
         
         json_demo.py,json_path,database.py is used for demo purposes.
         
          
               
