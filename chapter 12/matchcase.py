# introduced from py 3.10

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server error"
        case _ :
            return "please put input"
        

print(http_status(200))

#recoding again

def server_status(status):
    match status:
        case 500:
            return "ok"
        case 300:
            return "ggs"
        case 404:
            return "error"
        case _ :
            return "please provide input"
        
print(server_status(300))