import enum
import queue
import random
import numpy

class requestName(enum.Enum):
    mobileRequest = 0
    webRequest = 1
    sendMessage = 2
    restaurantMobile = 3
    restaurantWeb = 4
    courierRequest = 5
    followUp = 6
    
class microServices(enum.Enum):
    restaurantManagement = 0
    customerManagement = 1
    orderManagement = 2
    courierContact = 3
    payments = 4
    APIPort = 5
    webPort = 6
    
        
        
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
        self.instances = []
        self.arrivalTime = arrivalTime
        self.Type = self.generateType()
        services[self.Type.chain[0].value].requestArrival(self)
        # self.completed = False

    def generateType(self):
        prob = random.random()
        for i in range(len(requestProbs)):
            if prob*100 < requestProbs[i]:
                return typeRequests[i]
    
    def getNextService(self, previousService:microServices):
        for i,service in enumerate(self.Type.chain):
            if service == previousService:
                if i ==  len(self.Type.chain)-1:
                    return None
                return self.Type.chain[i+1]
            

class ServiceInstance:
    
    def __init__(self, Type) -> None:
        self.Type = Type
        self.active = False
        self.duration = 0
        self.timePassed = 0
        self.waiting = False
    
    def start(self, request:Request):
        print(request.arrivalTime,request.Type.requestName,self.Type,time)
        if len(request.instances) == 0:
            self.parentInstance = None
        else:
            self.parentInstance = request.instances[-1]
        self.active = True
        self.duration = round(numpy.random.exponential(meanServiceTimes[self.Type]))
        self.request= request

        next_service = request.getNextService(self.Type)
        if next_service == None:
            self.waiting = False
        else:
            self.waiting = True
            request.instances.append(self)
            services[next_service.value].requestArrival(request)

    def passTime(self):
        self.timePassed += 1
        if self.waiting:
            return
        self.duration -= 1
        if self.duration != 0:
            return
        self.active = False
        if self.parentInstance != None:
            self.parentInstance.waiting = False



        
    
        
        
    
    
class Service:
    def __init__(self,instanceNumber, Type) -> None:
        self.queue = []
        self.Type = Type
        self.instances = self.generateInstances(instanceNumber)
        
    def generateInstances(self,instanceNumber):
        result = []
        for _ in range(instanceNumber):
            result.append(ServiceInstance(self.Type))
        return result

    def requestArrival(self, request):
        find_instances = self.checkFreeInstances()
        
        if len(find_instances) == 0:
            self.queue.append(request)
        else:
            instance = random.choice(find_instances)
            instance.start(request)


    def checkFreeInstances(self):
        find_instances = []
        for instance in self.instances:
            if not instance.active:
                find_instances.append(instance)

        return find_instances
    def passTime(self):
        for service in self.instances:
            if service.active:
                service.passTime()
        if len(self.queue) == 0:
            return
        find_instances = self.checkFreeInstances()
        if len(find_instances) == 0:
            return
        random.shuffle(find_instances)
        for instance in find_instances:
            if len(self.queue) == 0:
                break
            request = self.queue.pop(0)
            instance.start(request)
        
        
        
        

service_instances = (list(map(int, input().split())))
request_rate = int(input())
duration = int(input())
max_time = (list(map(int, input().split()))) #optional

services = []
for i, instanceNum in enumerate(service_instances):
    services.append(Service(instanceNum, microServices(i)))

time = 0

for _ in range(duration):
    for _ in range(request_rate):
        request = Request(time)
        
    for service in services:
        service.passTime()
    time += 1
