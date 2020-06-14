
import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host =  "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor() 

cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'rain'")
results = cursor.fetchall()
print(results)
print(type(results))

def definition(word):
    statement = "SELECT * FROM Dictionary WHERE Expression ='" + word + "'"
    query = cursor.execute(statement)
   
    results = cursor.fetchall()
    
    if results:
        resultDefination = []
        for result in results:

            resultDefination.append(result[1])
        return resultDefination
    return "Incorrect word!"
"""
word = input("Enter word: ")

output = definition(word.lower())
if type(output) == list:
    for item in output:
        print("* ",item)
else:
    print(output)
    """