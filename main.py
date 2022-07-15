import enum
import random
import numpy

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
    
        
        
class TypeRequest():
    def __init__(self, name: requestName, chain, probability) -> None:
        self.requestName = name
        self.chain = chain
        self.probability = probability
        
typeRequests = [
    TypeRequest(requestName.mobileRequest,
            [microServices.APIPort,microServices.orderManagement,microServices.payments]
            ,0.2),
    TypeRequest(requestName.webRequest,
            [microServices.webPort,microServices.orderManagement,microServices.payments]
            ,0.1),
    TypeRequest(requestName.sendMessage,
            [microServices.APIPort,microServices.customerManagement,microServices.courierContact]
            ,0.05),
    TypeRequest(requestName.restaurantMobile,
            [microServices.APIPort,microServices.restaurantManagement]
            ,0.25),
    TypeRequest(requestName.restaurantWeb,
            [microServices.webPort,microServices.restaurantManagement]
            ,0.15),
    TypeRequest(requestName.courierRequest,
            [microServices.webPort,microServices.restaurantManagement,microServices.courierContact]
            ,0.2),
    TypeRequest(requestName.followUp,
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


class Request:
    def __init__(self, arrivalTime) -> None:
        self.arrivalTime = arrivalTime
        self.Type = self.generateType()
        # self.completed = False

    def generateType():
        prob = random.random()
        for i in len(requestProbs):
            if prob*100 < requestProbs[i]:
                return typeRequests[i]

class ServiceInstance:
    def __init__(self, Type) -> None:
        self.Type = Type
        self.active = False
    
    def start(self):
        self.active = True
        
        
    
    
class Service:
    def __init__(self,instanceNumber, Type) -> None:
        self.queue = []
        self.instances = self.generateInstances(instanceNumber)
        
        self.Type = Type
    def generateInstances(instanceNumber):
        result = []
        for _ in range(instanceNumber):
            result.append(ServiceInstance())
    def passTime():



service_instances = (list(map(int, input().split())))
request_rate = int(input())
duration = int(input())
max_time = (list(map(int, input().split()))) #optional

services = []
for i, instanceNum in enumerate(service_instances):
    services.append(Service(instanceNum, microServices(i+1)))

time = 0

for _ in range(duration):
    for _ in range(request_rate):
        request = Request(time)

    
    time += 1