def get_auth_token():
    import requests
    from requests.auth import HTTPBasicAuth 
    import env_lab
    import urllib3
    urllib3.disable_warnings()                                  #stops warning due to certificate unverification
    
    auth_api_endpoint = "dna/system/api/v1/auth/token"          #api endpoint/resource for authN
    url = f"{env_lab.DNA_CENTER["host"]}{auth_api_endpoint}"    #url for gx
    basic_authN = HTTPBasicAuth\
                    (username=env_lab.DNA_CENTER["username"], \
                    password=env_lab.DNA_CENTER["password"])    #authN username and password  

    response = requests.post(url, verify=False, auth=basic_authN)       #gx
    response = response.json()                                  #convert to python dict.
    token = response["Token"]                                   #store value of "Token" key as "token"

    print(token)                                                #print out token

    return token                                                #store token as value of the function

if __name__ == "__main__":
    get_auth_token()                                            #call the function

