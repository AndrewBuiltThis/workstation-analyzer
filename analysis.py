# -*- coding: utf-8 -*-
# Title :
# Objective :
# Author :
# Date : 
# ToS : 
# License :
# Additional Info : 

# Import Necessary Modules
import sys
import socket
import os
import dns.resolver
import psutil
import platform
import datetime
import json
import subprocess
import re
from jinja2 import Environment, FileSystemLoader

reportJSON = {
        "machineInfo": {
            "identity" : {
                "name" : None,
                "fqdn" : None,
                "ip" : None
            },
            "aliases" : [],
            "system" : {
                "os" : None,
                "osVersion" : None,
                "processor" : None,
                "specs" : None,
                "connectedUsers" : [],
                "lastReboot" : None
            },
            "networking" : {
                "pingTests" : {
                    "externalPing" : {
                        "externalUrl" : None,
                        "success" : None
                    },
                    "internalPing" : {
                        "internalUrl" : None,
                        "success" : None
                    }
                },
                "performanceTests" : None,
                "errors" : []
            },
            "performance" : {
                "cpu" : {
                    "cores" : None,
                    "cpuUsage" : None
                },
                "ram" : {
                    "totalRAM" : None,
                    "availableRAM" : None,
                    "ramUsage" : None
                },
                "disk" : {
                    "diskSpace" : None,
                    "diskUsage" : None
                }
            },
            "services" : {
                "active" : [],
                "inactive" : []
            }
        },
        "networkInfo" : {
            "domain" : None,
            "openPorts" : [],
            "public" : "UNKNOWN"    
        },
        "organizationInfo" : {
            "organizationName" : None,
            "organizationType" : None,
            "organizationSize" : None,
            "machineUser" : None,
            "organizationPointOfContact" : None
        },
        "testInfo" : {
            "gtgStaffName" : None,
            "gtgTestDatetime" : None,
            "gtgTestReason" : None
        }
    }

class clientMachine():

    def getGTGInfo(self,staff,reason):
        print("Begin Processing GTG Information ... ")
        reportJSON["testInfo"].update({"gtgStaffName" : str(staff)})
        reportJSON["testInfo"].update({"gtgTestDatetime" : str(datetime.datetime.now().strftime("%Y-%m-%d"))})
        reportJSON["testInfo"].update({"gtgTestReason" : str(reason)})
        print("GTG Information Processed Successfully!")

    def getOrgInfo(self,orgName,orgType,orgSize,orgPOC,machineUser):
        print("Begin Processing Organizational Information ... ")
        reportJSON["organizationInfo"].update({"organizationName" : str(orgName)})
        reportJSON["organizationInfo"].update({"organizationType" : str(orgType)})
        reportJSON["organizationInfo"].update({"organizationSize" : str(orgSize)})
        reportJSON["organizationInfo"].update({"organizationPointOfContact" : str(orgPOC)})
        reportJSON["organizationInfo"].update({"machineUser" : str(machineUser)})
        print("Organization Information Processed Successfully!")

    def getMachineInfo(self):
        print("Begin Processing Machine Information ... ")
        reportJSON["machineInfo"]["identity"].update({"name" : socket.gethostname()})
        reportJSON["networkInfo"].update({"domain" : socket.getfqdn()})
        reportJSON["machineInfo"]["identity"].update({"fqdn" : socket.getfqdn()})
        reportJSON["machineInfo"]["identity"].update({"ip" : socket.gethostbyname(socket.gethostname())})
        reportJSON["machineInfo"]["system"].update({"os" : platform.system()})
        reportJSON["machineInfo"]["system"].update({"osVersion" : platform.release()})
        reportJSON["machineInfo"]["system"].update({"processor" : platform.processor()})
        reportJSON["machineInfo"]["system"].update({"specs" : platform.architecture()[0]})
        reportJSON["machineInfo"]["system"].update({"connectedUsers" : psutil.users()})
        reportJSON["machineInfo"]["system"].update({"lastReboot" : datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d")})
        print("Machine Information Processed Successfully!")

    def pingMachine(self, ip, port , googleEndpoint="172.217.7.206"):
        print("Begin Ping Tests ... ")
        connSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connSocket.connect((ip, port))
            reportJSON["machineInfo"]["networking"]["pingTests"]["internalPing"].update({"internalUrl" : ip,"success" : True})
            print("Internal Machine Pinged Successfully!")
        except:
            reportJSON["machineInfo"]["networking"]["pingTests"]["internalPing"].update({"internalUrl" : ip,"success" : False})
            print("Internal Machine Could Not Be Pinged!")
        try:
            connSocket.connect((googleEndpoint, port))
            reportJSON["machineInfo"]["networking"]["pingTests"]["externalPing"].update({"externalUrl" : googleEndpoint,"success" : True})
            print("External Machine Pinged Successfully!")
        except:
            reportJSON["machineInfo"]["networking"]["pingTests"]["externalPing"].update({"externalUrl" : googleEndpoint,"success" : False})
            print("External Machine Could Not Be Pinged!")
        connSocket.close()

    def testNetwork(self, externalEndpoint="github.com" , lanEndpoint=None , wanEndpoint=None , googleEndpoint="google.com" ):
        print("Begin Gathering Network Statistics ...")
        i = 0
        pingArray = []
        testEndpoints = [googleEndpoint , externalEndpoint , lanEndpoint , wanEndpoint]
        endpointTypes = ["google" , "external" , "lan" , "wan"]
        for url in testEndpoints:
            networkTest = {
                "endpoint" : url,
                "type" : str(endpointTypes[i]),
                "results" : {
                    "resolvingEndpoint" : None,
                    "resolvingIp" : None,
                    "pingFailurePercent" : None,
                    "avgResponseTime" : None,
                    "minResponseTime" : None,
                    "maxResponseTime" : None                }
            }
            i += 1
            if url !=None:
                try:
                    hostPattern = r"Pinging (.*?) \["
                    ipPattern = r"\[(.*?)\]"
                    lossPattern = r", Lost = (.*?) \("
                    minPattern = r"Minimum = (.*?)\m"
                    maxPattern = r"Maximum = (.*?)\m"
                    avgPattern = r"Average = (.*?)\m"
                    latencyResponse = subprocess.check_output("ping -n 10 " + url , shell=True)
                    if latencyResponse == 0:
                        print(latencyResponse)
                        networkTest["results"].update({"resolvingEndpoint" : re.search(hostPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"resolvingIp" : re.search(ipPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"pingFailurePercent" : re.search(lossPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"avgResponseTime" : re.search(avgPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"minResponseTime" :re.search(minPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"maxResponseTime" : re.search(maxPattern, latencyResponse).group(1)})
                        pingArray.append(networkTest)
                    else:
                        networkTest["results"].update({"resolvingEndpoint" : re.search(hostPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"resolvingIp" : re.search(ipPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"pingFailurePercent" : re.search(lossPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"avgResponseTime" : re.search(avgPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"minResponseTime" :re.search(minPattern, latencyResponse).group(1)})
                        networkTest["results"].update({"maxResponseTime" : re.search(maxPattern, latencyResponse).group(1)})
                        pingArray.append(networkTest)
                except:
                    print("An Error Occured.")
                    pingArray.append(networkTest)
            else:
                pingArray.append(networkTest)
            reportJSON["machineInfo"]["networking"].update({"performanceTests" : pingArray})
        print("Network Statistics Successfully Gathered!")
        print("Begin Gathering Network Information ... ")
        networkStatisticsArray = psutil.net_io_counters(pernic=True)
        for network in networkStatisticsArray:
            result = {
                "networkId" : network,
                "inboundErrors" : networkStatisticsArray[network][4],
                "outboundErrors" : networkStatisticsArray[network][5],
                "inboundDrops" : networkStatisticsArray[network][6],
                "outboundDrops" : networkStatisticsArray[network][7]
            }
            reportJSON["machineInfo"]["networking"]["errors"].append(result)
        print("Network Information Successfully Gathered!")
        
    def getDNSAliases(self):
        print("Begin Collecting DNS Information ... ")
        machineName = socket.gethostname()
        resolver = dns.resolver.Resolver()
        try:
            result = resolver.query(machineName , "A")
            aliasArray = []
            for index in range(len(result)):
                aliasArray.append(str(result[index]))
            reportJSON["machineInfo"].update({"aliases" : aliasArray})
            print("Successully Collected DNS Information!")
        except:
            reportJSON["machineInfo"].update({"aliases" : ["UNKNOWN"]})
            print("DNS Information Could Not Be Obtained ... Continuing ... ")

    def getPerformanceMetrics(self):
        reportJSON["machineInfo"]["performance"]["cpu"].update({"cores" : psutil.cpu_count()})
        
        reportJSON["machineInfo"]["performance"]["cpu"].update({"cpuUsage" : psutil.cpu_percent()})
        
        ramUtilization = dict(psutil.virtual_memory()._asdict())
        reportJSON["machineInfo"]["performance"]["ram"].update({"totalRAM" : ramUtilization['total']})
        
        reportJSON["machineInfo"]["performance"]["ram"].update({"availableRAM" : ramUtilization['available']})
        
        reportJSON["machineInfo"]["performance"]["ram"].update({"ramUsage" : ramUtilization['percent']})
        
        reportJSON["machineInfo"]["performance"]["disk"].update({"disks" : psutil.disk_partitions(all=False)})
        
        reportJSON["machineInfo"]["performance"]["disk"].update({"diskSpace" : psutil.disk_usage('/')[0]})
        
        reportJSON["machineInfo"]["performance"]["disk"].update({"diskAvailable" : psutil.disk_usage('/')[2]})
        
        reportJSON["machineInfo"]["performance"]["disk"].update({"diskUsage" : psutil.disk_usage('/')[3]})
        

    def getWindowsServices(self):
        print("Begin Collecting Started Windows Services ... ")
        serviceArray = psutil.win_service_iter()
        for service in serviceArray:
            try:
                serviceDetails = psutil.win_service_get(service._name)
                serviceDict = serviceDetails.as_dict()
                if(serviceDict["status"] == "running"):
                    service = {}
                    if(serviceDict["display_name"] != None):
                        service["name"] = serviceDict["display_name"]
                    if(serviceDict["username"] != None):
                        service["user"] = serviceDict["username"]
                    if(serviceDict["pid"] != None):
                        service["pid"] = serviceDict["pid"]
                    service["status"] = serviceDict["status"]
                    reportJSON["machineInfo"]["services"]["active"].append(service)
                if(serviceDict["status"] == "stopped"):
                    service = {}
                    if(serviceDict["display_name"] != None):
                        service["name"] = serviceDict["display_name"]
                    if(serviceDict["username"] != None):
                        service["user"] = serviceDict["username"]
                    service["status"] = serviceDict["status"]
                    reportJSON["machineInfo"]["services"]["inactive"].append(service)
            except:
                print("Could Not Record Windows Services ... Moving On ... ")
        print("Successfully Recorded Windows Services!")

    def getOpenPorts(self):
        print("Begin Scanning Local Ports ... ")
        try:
            openPortArray = []
            for port in range(1,3025):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(socket.gethostbyname(socket.gethostname()), port)
                if result == 0:
                    openPortArray.append(port)
                sock.close()
            reportJSON["networkInfo"].update({"openPorts" : openPortArray})
            print("Network Ports Successfully Scanned!")
        except:
            print("Unable to Scan Ports ... Continuing ... ")
            reportJSON["networkInfo"].update({"openPorts" : ["ERROR. UNABLE TO SCAN PORTS."]})
    
    def generateMachineReport(self):
        # Recieve Input from Batch Script and Save as Scoped Variables
        testingUser = sys.argv[1]
        testingReason = sys.argv[2]
        clientOrganization = sys.argv[3]
        clientType = sys.argv[4]
        clientSize = sys.argv[5]
        clientPOC = sys.argv[6]
        clientMachineOwner = sys.argv[7]
        pingIP = sys.argv[8]
        networkPort = int(sys.argv[9])
        externalUrl = sys.argv[10]
        print(externalUrl)
        if(sys.argv[11] == "EMPTYURLPARAMETER"):
            lanURL = None
        else:
            lanURL = sys.argv[11]
        if(sys.argv[12] == "EMPTYURLPARAMETER"):
            wanURL = None
        else:
            wanURL = sys.argv[12]
        self.getGTGInfo(staff=testingUser , reason=testingReason) 
        self.getOrgInfo(orgName=clientOrganization , orgType=clientType , orgSize=clientSize , orgPOC=clientPOC , machineUser=clientMachineOwner)
        self.getMachineInfo()
        self.pingMachine(ip=pingIP , port=networkPort)
        self.testNetwork(externalEndpoint=externalUrl , lanEndpoint=lanURL , wanEndpoint=wanURL)
        self.getPerformanceMetrics()
        self.getWindowsServices()
        self.getOpenPorts()
        self.getDNSAliases()
        print("Obtaining Local Machine Statistics Completed!")
        print("Writing Statistics to JSON ... ")
        with open('output/results.json', 'w') as fp:
            json.dump(reportJSON, fp, sort_keys=True, indent=4)
        fp.close()
        print("JSON File Created!")
        root = os.path.dirname(os.path.abspath(__file__))
        fileLoader = FileSystemLoader('templates')
        env = Environment(loader=fileLoader)
        template = env.get_template('template.html')
        performanceResults = ["Empty" , "Empty" , "Empty" , "Empty"]
        for result in range(len(reportJSON['machineInfo']['networking']['performanceTests'])):
            performanceResults[result] = reportJSON['machineInfo']['networking']['performanceTests'][result]
        output = template.render(
            machineName=reportJSON['machineInfo']['identity']['name'],
            analysisDate=reportJSON['testInfo']['gtgTestDatetime'],
            analysisUser=reportJSON['testInfo']['gtgStaffName'],
            analysisReason=reportJSON['testInfo']['gtgTestReason'],
            machineOS=reportJSON['machineInfo']['system']['os'],
            machineOSVersion=reportJSON['machineInfo']['system']['osVersion'] ,
            machineProcessor= reportJSON['machineInfo']['system']['processor'], 
            machineIP = reportJSON['machineInfo']['identity']['ip'],
            machineFQDN= reportJSON['machineInfo']['identity']['fqdn'],
            machineOwner= reportJSON['organizationInfo']['machineUser'], 
            googleEndpoint= reportJSON['machineInfo']['networking']['performanceTests'][0]['endpoint'],
            googleIP= reportJSON['machineInfo']['networking']['performanceTests'][0]['results']['resolvingIp'],
            googleMinResponse= reportJSON['machineInfo']['networking']['performanceTests'][0]['results']['minResponseTime'],
            googleAvgResponse= reportJSON['machineInfo']['networking']['performanceTests'][0]['results']['avgResponseTime'], 
            googleMaxResponse= reportJSON['machineInfo']['networking']['performanceTests'][0]['results']['maxResponseTime'],
            totalStorage= (int(reportJSON['machineInfo']['performance']['disk']['diskSpace'])/1073741824),
            storageInUse = reportJSON['machineInfo']['performance']['disk']['diskUsage'],
            remainingStorage= (int(reportJSON['machineInfo']['performance']['disk']['diskAvailable'])/1073741824),
            cpuCount= reportJSON['machineInfo']['performance']['cpu']['cores'],
            cpuInUse=reportJSON['machineInfo']['performance']['cpu']['cpuUsage'],
            totalRAM= (int(reportJSON['machineInfo']['performance']['ram']['totalRAM'])/1073741824), 
            ramInUse= reportJSON['machineInfo']['performance']['ram']['ramUsage'],
            availableRAM= (int(reportJSON['machineInfo']['performance']['ram']['availableRAM'])/1073741824), 
            orgType= reportJSON['organizationInfo']['organizationType'], 
            orgSize= reportJSON['organizationInfo']['organizationSize'], 
            orgPOC= reportJSON['organizationInfo']['organizationPointOfContact'], 
            orgName=reportJSON['organizationInfo']['organizationName'],
            networkTestResults = reportJSON['machineInfo']['networking']['performanceTests'],
            networkErrors = reportJSON['machineInfo']['networking']['errors'],
            windowsServices = reportJSON['machineInfo']['services']['active'],
            connectedUsers = reportJSON['machineInfo']['system']['connectedUsers']
            )
        filename = os.path.join(root, 'output', 'index.html')
        with open(filename, 'w') as fh:
            fh.write(output)
            print("HTML File Created")
        print("Analysis Complete! Review the JSON File For Results!")

if __name__ == '__main__':
    print("Initializing Application Class ... ")
    app = clientMachine()
    print("Beginning Client Machine Analysis ... ")
    app.generateMachineReport()
    print("Generating Report ... ")