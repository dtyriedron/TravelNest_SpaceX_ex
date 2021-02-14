import requests
import json

# get the data from the latest launch
launch_response = requests.get("https://api.spacexdata.com/v4/launches/latest")
# parse json
launch_json_response = launch_response.json()
# print genral launch details
print(
    "latest launch",
    "\tname: "+launch_json_response["name"], 
    "\tdetails: "+launch_json_response["details"],
    "\tdate: "+launch_json_response["date_utc"], sep="\n"
    )
# store the ships json object 
ships = launch_json_response["ships"]
# retrieve each ship and print its details
ship_counter = 1
print("\nships: ")
for ship in ships:
    # format print statement to print the index of the ship in the right place
    print("{}{}{}".format("\n\tship", ship_counter, ": "))
    # use the ship id to get the reponse for that ship
    ship_response = requests.get("https://api.spacexdata.com/v4/ships/"+ship)
    # print ship details
    print(
        "\tname: "+ship_response.json()["name"],
        "\ttype: "+ship_response.json()["type"],
        "\thome port: "+ ship_response.json()["home_port"],
        sep="\n"
    )
    # increase ship counter 
    ship_counter+=1

