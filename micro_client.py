# Zach Orlosky
# Orloskyz@oregonstate.edu
# CS 361

import requests
import json

def main():
    """
    Plant microservice using Flask for HTTP endpoint
    """
    print("PLANT MICROSERVICE\n")

    while True:
        print("Select an option:\n")
        print("1 - Get plant info")
        print("2 - Get available plant names")
        print("3 - Exit\n")

        option = input()

        if option == '1':
            plant_name = input("Enter plant name: ")
            print()
            request = {'info': 'get_plant_info', 'name': plant_name}
            response = requests.post('http://localhost:5555/api', json=request)
            print(response.json())
            print()

        elif option == '2':
            request = {'info': 'get_plant_list'}
            response = requests.post('http://localhost:5555/api', json=request)
            print(response.json())
            print()

        elif option == '3':
            request = {'info': 'exit'}
            response = requests.post('http://localhost:5555/api', json=request)
            print(response.json())
            break

        else:
            print("Please select a number 1 to 3!\n")

if __name__ == "__main__":
    main()
