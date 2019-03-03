#writed by moein
#test system is connecting yes or no
from requests import get, exceptions
try:
    get("https://google.com", timeout=3)
    print(20*"-")
    print("conndect")
    print(20*"-")
except exceptions.ConnectionError:
    print(20*"-")
    print("not connect")    
    print(20*"-")
#thise is python's power    