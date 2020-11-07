'''
    This is a library for the Ethereum network API that will simplify the process of pulling information
    from their funky API that dumb dumbs like me refuse to try to learn. It will also make decisions for
    you like is a worker active and maybe even decide the slope of your recent mining.

    Intended for use with Ethpool, Ethermine & Flypool pools.
'''

import requests

class General:
    def __init__(self, address):
        address = str(address)
        response = requests.get("https://api.ethermine.org/miner/" + address + "/dashboard") # All data for general information, not miner specific

        # Response for could not find API address so not good :/
        if response.status_code == 404:
            print("Could not find miner. Make sure you entered the address correctly and try again.")
            exit()

        # Response for good :) Now it will run all the data determining and whatnot
        elif response.status_code == 200:
            data = response.json()

        # Uho, one of the other many return codes I neglected to prepare this code for :/ good luck bubs
        else:
            print("API request returned with code: " + response.status_code + ". Sorry :/")
            exit()


# Technically the data for the miners is available to the general class, but this breaks it up more and makes it easier to work with I think? hope?
class Worker:
    def __init__(self, address, workerName):
        address = str(address)
        response = requests.get("https://api.ethermine.org/miner/" + address + "/dashboard") # All data for general information, not miner specific

        # Response for could not find API address so not good :/
        if response.status_code == 404:
            print("Could not find miner. Make sure you entered the address correctly and try again. Also confirm you are sending the miner address as type String.")
            exit()

        # Response for good :) Now it will run all the data determining and whatnot
        elif response.status_code == 200:
            data = response.json()

            # API is a behind and lets you pull from it with a code 200 but still fail with an incorrect address, ew
            if data["status"] == "ERROR":
                print("Could not find miner. Make sure you entered the address correctly and try again. Also confirm you are sending the miner address as type String.")
                exit()

            workers = data["data"]["workers"] # way shortens this for readibiltyh

            # The most difficult way possible to pull the placement of the worker in the list
            if len(workers) > 1:
                workerNumber = 0
                for worker in workers:
                    if worker["worker"] == workerName:
                        break
                    else:
                        workerNumber += 1
                        if workerNumber == len(workers):
                            print("Worker name was not found. Please check your spelling and try again.")
                            exit()
            else:
                workerNumber = 0

            self.workerName = workers[workerNumber]["worker"]


        # Uho, one of the other many return codes I neglected to prepare this code for :/ good luck bubs
        else:
            print("API request returned with code: " + respone.status_code + ". Sorry :/")
            exit()


# Test cases :D
if __name__ == '__main__':
    generalTest = General("0x2E5Acdc5C6F1083c4d6127a6b41e6BDB24b6b8E0")
    workerTest = Worker("0x2E5Acdc5C6F1083c4d6127a6b41e6BDB24b6b8E0", "thotbox")

    print(workerTest.workerName)
