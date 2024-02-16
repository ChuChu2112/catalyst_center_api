def get_auth_token():
    import requests
    from requests.auth import HTTPBasicAuth #import function for making simple web authentications
    import env_lab  #import external file containing needed information and credentials
    import json

    requests.packages.urllib3.disable_warnings()    #try to suppress error messages due to SSL certificate invalidation
    
    auth_api_endpoint = "dna/system/api/v1/auth/token"  #store dna center api endpoint/resource
    
    url = f"{env_lab.DNA_CENTER["host"]}{auth_api_endpoint}"    #build the url

#     headers = {
#     'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
#     }

    #make the POST request, including the HTTPBasicAuth call as the 'auth' argument
    response = requests.post(url=url, auth=HTTPBasicAuth(env_lab.DNA_CENTER["username"], env_lab.DNA_CENTER["password"]))
    
    response = json.loads(response) #convert to python dict.

    token = response["Token"]   #index the token key in the python dictionary and store as 'token'

    print(token)    #print out token
    return token    #store token as value of the function

get_auth_token()    #call the function

#The token response from POSTMAN:
#{"Token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTcwNzc3Nzg0MywiaWF0IjoxNzA3Nzc0MjQzLCJqdGkiOiI4Yzc5OWMyNy0zNzI4LTRiNTItYmI1Yy1lMzg3ZDY5MzM0NmMiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.ipnt9_l9SUnB_IWU5y84Yczdk-Gpj72jvm3UV9aEKXE5ymOCKJq46Q9IM2PmrHkEyiS9mdlnhHax_0OciC6BXxh_OU53B14gR0QPsr2k0SP6E-hiN_B3cZsRNriEeNrMiVsQrF0RZoXLhWTROH72jXyNnp0BlIUcMNHUoUHJrtylzbRX8tnBqzeiSena2QX8wTZ5jvRki4Aks_eL9x16LEN_uw6lZVA6gagsZrsTYZhQbO1G4CkkBjhF6-E__TwHSrCMjPoUxwylr_RFR4VbuBjAHx0oviJYw7HkPpG6iDJjQuiOHwKvQ9EazhpJgmTnBADqchgmjrTfABdx0ConWg"}

