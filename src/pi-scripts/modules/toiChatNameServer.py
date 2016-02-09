#!/usr/bin/env python3

# 
# Python toiChat Front-End Runner
#   Script interacts with background services such as toiChatServer and
#   toiChatClient.
#
#
# Created on: 02/07/2016
# Author: Toi-Group
#

from modules.protobuf import ToiChatProtocol_pb2 # Used for DnsMessage 
                                                 # Protocol
from modules.toiChatClient import toiChatClient # Used for replying to 
                                                # received messages
import time # Used for documenting the local time of the DNS register
import socket, struct, fcntl # Used for resolving local IP address

class toiChatNameServer():
    # Types of commands to expect
    #
    getCommand={
        0:"register",
        1:"request"
    }

    #constructor
    # Creates a DNS when a toiChatNameServer object is instantiated.
    # and adds its own name, ipv4 address, and description to the dns
    # lookup table
    #
    def __init__(self, xtoiChatClient):
        # Store ToiChatClient to used to send dns messages
        #
        self.myToiChatClient = xtoiChatClient
        
        # Define dictionary to hold values of user name
        # and key pairing of IP and other relevant information
        # User name will be keys of the dictionary while the values
        # will be the IPs of the user
        #
        # DICTIONARY FORMAT:
        # self.dns = {
        #     clientname0 = {
        #         clientId = IPv4 address
        #         lastUpdate = <DATE OF LAST UPDATE>
        #         description = <MISC INFOMATION OF CLIENT>
        #     }
        #     clientname1 = {
        #         clientId = IPv4 address
        #         lastUpdate = <DATE OF LAST UPDATE>
        #         description = <MISC INFOMATION OF CLIENT>
        #     }
        #     clientname2 = {
        #         clientId = IPv4 address
        #         lastUpdate = <DATE OF LAST UPDATE>
        #         description = <MISC INFOMATION OF CLIENT>
        #     }
        #     ... LIST CAN GROW ...
        # }
        #
        #
        #
        self.dns = {}

        # Register local machine in DNS replacing any old values
        #
        self.addToDNS(self.myToiChatClient.getName(), self.getMyIP(), \
            time.strftime("%Y%m%d - %H:%M:%S"), \
            self.myToiChatClient.getDescription())


    # Returns the IPv4 address of the local machine for the given interface
    # 
    # Sourced from: http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    def getMyIP(self, iface = 'eth0'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd = sock.fileno()
        SIOCGIFADDR = 0x8915
        ifreq = struct.pack('16sH14s', iface.encode('utf-8'), \
            socket.AF_INET, b'\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
        except:
            return None
        ip = struct.unpack('16sH2x4s8x', res)[2]
        return socket.inet_ntoa(ip)

    # Adds one client to the internal dictionary
    #
    def addToDNS(self, clientName, clientId, lastUpdate, description):
        # Update dictionary with passed information
        #
        self.dns[clientName] = {}
        self.dns[clientName]['clientId'] = clientId
        self.dns[clientName]['lastUpdate'] = lastUpdate
        self.dns[clientName]['description'] = description
        return 1

    # method to return IP of user the client is attempting to contact
    # returns 'None' if IP does not exist
    #   
    def lookupIPByHostname(self, userHostname):
        return self.dns[userHostname]['clientId']

    # method to return IP of user the client is attempting to contact
    # returns 'None' if IP does not exist
    #   
    def lookupHostnameByIP(self, userIP):
        for hostname in self.dns:
            if self.dns[hostname]['clientId'] == userIP:
                return hostname
        return None

    # Updates the current machines hostname entry in the internal dictionary
    #
    #   
    def updateMyName(self, oldName, newName):
        return self.addToDNS(newName, self.getMyIP(), \
            time.strftime("%Y%m%d - %H:%M:%S"), \
            self.lookupHostnameByIP(oldName))

    # Print the current dns lookup table to the console
    #
    def printDNSTable(self):
        print(self.dns)
        return 1

    # Handle DnsMessage type received from a toiChatServer instance.  
    # Message type is already known to be DNS message
    #
    def handleDnsMessage(self, myDnsMessage):
        if myDnsMessage.command == self.getCommand[0]:
            self.handleRegisterDNS(myDnsMessage)
        elif myDnsMessage.command == self.getCommand[1]:
            self.handleRequestDNS(myDnsMessage)
        else:
            print("Unknown DNSMessage Command. '" + \
                str(myDnsMessage.command) + "'")
            return 0
        return 1

    # Extract the name, ipv4 address, last update, and misc information from 
    # DNS message and register into local DNS
    #
    def handleRegisterDNS(self, registerDNSMessage):
        # Loop through all repeated clients in DnsMessage
        #
        for newClient in registerDNSMessage.clients:
            # Check if user is in the DNS already
            #
            if newClient.clientName in self.dns:
                # If user is already in DNS do nothing
                #
                continue
            else:
                self.addToDNS(newClient.clientName, newClient.clientId, \
                    newClient.lastUpdate, newClient.description)
        return 1

    # Handles a DnsMessage from a client who is requesting our DNS table.
    # Returns a registerDNS message to the client
    #
    def handleRequestDNS(self, requestDNSMessage):
        # Get the information about the client requesting DNS information
        #
        returnAddress = requestDNSMessage.clientId

        # Create a new Register DNS Message
        #
        myRequestDNS = self.createRegisterDnsMessage()

        # Send message back to requester
        #
        self.myToiChatClient.sendMessage(returnAddress, myRequestDNS)
        
        return 1        
  
    # Send our DNS table to another machine
    # Populate a DnsMessage Register message type with information about
    # each client in our DNS table. 
    #
    def createRegisterDnsMessage(self):
        # Create a template DNS message
        #
        registerDNS = self.createTemplateDnsMessage()

        # Populate the command command with status of "register"
        #
        registerDNS.dnsMessage.command = self.getCommand[0]

        # Create a DNSclient message for each client in our DNS dictionary
        #
        registerDNSClient = ToiChatProtocol_pb2.DnsMessage.DNSClients()

        # Populate our registerDNS message with DNSClients from our
        # DNS dictionary
        #
        for hostname in self.dns:
            registerDNSClient = registerDNS.dnsMessage.clients.add()
            registerDNSClient.clientName = hostname
            registerDNSClient.clientId  = self.dns[hostname]['clientId']
            registerDNSClient.lastUpdate = self.dns[hostname]['lastUpdate']
            registerDNSClient.description = self.dns[hostname]['description']
 
        # Return DnsMessage Type
        #
        return registerDNS
   
    # Create a message requesting the DNS table from another machine
    #
    def createRequestDnsMessage(self):
        # Create a template DNS message
        #
        requestDNS = self.createTemplateDnsMessage()

        # Populate the command we will use in the message with the
        # request dnsMessage value
        #
        requestDNS.dnsMessage.command = self.getCommand[1]

        #return requestDNS message
        #
        return requestDNS    

    # Create a message populating the headers of the DnsMessage type
    # with this client information.
    #
    def createTemplateDnsMessage(self):
        # Create new ToiChatMessage
        #
        myDnsMessage = ToiChatProtocol_pb2.ToiChatMessage()

        # Get the client name
        #
        myName = self.myToiChatClient.getName()
        
        # Fill myDnsMessage message with my information
        #
        myDnsMessage.dnsMessage.clientName = myName
        myDnsMessage.dnsMessage.clientId = self.dns[myName]['clientId']
        myDnsMessage.dnsMessage.lastUpdate = self.dns[myName]['lastUpdate']
        myDnsMessage.dnsMessage.description = self.dns[myName]['description']

        return myDnsMessage
