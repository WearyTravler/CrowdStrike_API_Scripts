from falconpy import Hosts


proxies = {
    "http": "REDACTED"
}

environment = {
    "prefix": "REDACTED_",
    "id_name": "REDACTED",
    "secret_name": "REDACTED"
}

falcon = Hosts(environment=environment,
               proxy=proxies,
                      base_url="https://REDACTED",
                      ssl_verify=False,
                      timeout=(3.05,26.95),
                      user_agent="Development",
                      debug=False
               )


def enable_detections(hostname):
    try:
        #Get aid of the requested host
        # print("Getting aid...")
        aid = falcon.query_devices_by_filter(
                    filter=f"hostname:'{hostname}*'"
                    )["body"]["resources"][0]
        print("The aid of",hostname, "is:",aid)
        #Disabling detections:
        enable_detections = falcon.PerformActionV2(action_name="detection_unsuppress",ids=aid)
        print("Enabled detections for", hostname)
        
    except IndexError:
        print("Error: Host does not exist.")

def main():
    #Get the hostname the user wants:
    hostname = input("What is the hostname you need detections enabled: ")
    enable_detections(hostname)


if __name__ == "__main__":
    main()
