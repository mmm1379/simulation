import enum
import random
import enum

class requestName(enum.Enum):
    mobileRequest = 1
    webRequest = 2
    sendMessage = 3
    restaurantMobile = 4
    restaurantWeb = 5
    courierRequest = 6
    followUp = 7
    
class microServices(enum.Enum):
    restaurantManagement = 1
    customerManagement = 2
    orderManagement = 3
    courierContact = 4
    payments = 5
    APIPort = 6
    webPort = 7
    
        
        
class Request():
    def __init__(self, name:requestName, chain, probability) -> None:
        self.requestName = name
        self.chain = chain
        self.probability = probability
        
Requests = [
    Request(requestName.mobileRequest,
            [microServices.APIPort,microServices.orderManagement,microServices.payments]
            ,0.2),
    Request(requestName.webRequest,
            [microServices.webPort,microServices.orderManagement,microServices.payments]
            ,0.1),
    Request(requestName.sendMessage,
            [microServices.APIPort,microServices.customerManagement,microServices.courierContact]
            ,0.05),
    Request(requestName.restaurantMobile,
            [microServices.APIPort,microServices.restaurantManagement]
            ,0.25),
    Request(requestName.restaurantWeb,
            [microServices.webPort,microServices.restaurantManagement]
            ,0.15),
    Request(requestName.courierRequest,
            [microServices.webPort,microServices.restaurantManagement,microServices.courierContact]
            ,0.2),
    Request(requestName.followUp,
            [microServices.APIPort,microServices.orderManagement]
            ,0.05)
]

meanServiceTimes = {
    microServices.restaurantManagement: 8,
    microServices.customerManagement  : 5,
    microServices.orderManagement     : 6,
    microServices.courierContact      : 9,
    microServices.payments            : 12,
    microServices.APIPort             : 2,
    microServices.webPort             : 3,
}


requestProbs = [20,10,5,25,15,20,5]
for i in range(1,len(requestProbs)):
    requestProbs[i] += requestProbs[i-1]

def generateRequest():
    prob = random.random()
    for i in requestProbs:
        if prob*100 < i:
            return i
    

service_instances = (list(map(int, input().split())))
request_rate = int(input())
duration = int(input())
max_time = (list(map(int, input().split()))) #optional


for _ in range(duration):
    for _ in range(request_rate):
        