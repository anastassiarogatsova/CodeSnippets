import pymysql
import json

def databaseOperations():
    connection = pymysql.connect(
        host="*",
        user="*",
        password="*",
        database="*")
    cursor = connection.cursor()

    with open('stops.txt') as f:
        json_string = json.load(f)
    
        for i in json_string:
            insert = "INSERT INTO Stops(stop_id, stop_code, stop_name, stop_lat, stop_lon, zone_id, alias, stop_area, stop_desc, lest_x, lest_y, zone_name, authority) VALUES(" + '"' + str(i['stop_id']) + '"'  + ", " + '"' + str(i['stop_code']) + '"' + ", " + '"' + str(i['stop_name']) + '"' + ", " + '"'  + str(i['stop_lat']) +  '"' + ", " + '"' + str(i['stop_lon']) + '"' +", " + '"'  + str(i['zone_id']) + '"' + ", " + '"' + str(i['alias']) + '"' + ", " + '"' + str(i['stop_area']) + '"'  + ", " + '"' + str(i['stop_desc']) + '"'  + ", " + '"' + str(i['lest_x']) + '"'  + ", " + '"' + str(i['lest_y']) + '"'  + ", " + '"' + str(i['zone_name']) + '"'  + ", " + '"' + str(i['authority']) + '"' + ");"
            cursor.execute(insert)
            
        connection.commit()
        connection.close()
        print("Values are added!")
        print("MySQL connection is closed")
        


databaseOperations()
#print("INSERT INTO Routes(route_id, agency_id, route_short_name, route_long_name, route_type, route_color, competent_authority) VALUES(" + 'hghg' + ", " + '3' + ", " + 'kfjkf' + ", " + "ldjfhjd" + ", " + "juhygtfr" + ", " + "fjfjjdkjf" + ", " + "gkifjff" + ");")


