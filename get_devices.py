#!/usr/bin/python3

import requests

def meraki_get(resource):

    api_path = "https://dashboard.meraki.com/api/v0"
    headers = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    response = requests.get(f"{api_path}/{resource}", headers=headers)

    response.raise_for_status()

    return response.json()


def main():

    orgs = meraki_get("organizations")
    print("\nOrganizations discovered: ")

    devnet_id = 0
    for org in orgs:
        id = org["id"]
        name = org["name"]
        print(f"ID: {id} Name: {name}")
        if "devnet" in name.lower():
            devnet_id = id
    print("-" * 50)

    if devnet_id:
        networks = meraki_get(f"organizations/{devnet_id}/networks")
        
        for network in networks:
            id = network["id"]
            name = network["name"]
            print(f"Network ID: {id} Name: {name}")
            if "devnet" in name.lower():
                devnet_network = id
        print("-" * 50)
                
    if devnet_network:
        devices = meraki_get(f"networks/{devnet_network}/devices")
        
        for device in devices:
            model = device["model"]
            ip = device["lanIp"]
            print(f"Model: {model} IP: {ip}")
        

if __name__ == "__main__":
    main()