from wakeonlan import send_magic_packet
import os
import os.path
import shutil
import sys
import win32wnet
import ctypes
import win32security
import win32api
import sys
import time
from ntsecuritycon import *

hostNames = [
    None                    #0
    ,None                   #1
    ,None                   #2
    ,'ZAKZRHB-CLLB3'        #3
    ,'ZAKZRHB-CLLB4'        #4
    ,'ZAKZRHB-CLLB5'        #5
    ,'ZAKZRHB-CLLB6D'       #6
    ,'ZAKZRHB-CLLB7'        #7
    ,'ZAKZRHB-CLLB8'        #8
    ,'ZAKZRHB-CLLB9D'       #9
    ,'ZAKZRHB-CLLB10D'      #10
    ,'ZAKZRHB-CLLB11D'      #11
    ,'ZAKZRHB-CLLB12D'      #12
    ,'ZAKZRHB-CLLB13D'      #13
    ,'ZAKZRHB-CLLB14D'      #14
    ,'ZAKZRHB-CLLB15D'      #15
    ,'ZAKZRHB-CLLB16D'      #16
    ,'ZAKZRHB-CLLB17'       #17
    ,'ZAKZRHB-CLLB18'       #18
    ,'ZAKZRHB-CLLB19'       #19
    ,'ZAKZRHB-CLLB20D'      #20
    , None                  #21
    ,'ZAKZRHB-CLLB22D'      #22
    ,'ZAKZRHB-CLLB23D'      #23
    ,'ZAKZRHB-CLLB24'       #24
    ]
#    ,'ZAKZRHB-CLL21D'       #21 --unplugged
macAddresses = [
    None                    #0
    ,None                   #1
    ,None                   #2
    ,'10-E7-C6-37-EA-C3'    #3
    ,'10-E7-C6-37-EA-CE'    #4
    ,'10-E7-C6-37-EA-DC'    #5
    ,'10-E7-C6-37-EA-B5'    #6
    ,'10-E7-C6-37-EB-19'    #7
    ,'10-E7-C6-37-EA-DA'    #8
    ,'9C-7B-EF-53-B3-66'    #9
    ,'9C-7B-EF-53-44-ED'    #10
    ,'9C-7B-EF-53-B5-91'    #11
    ,'9C-7B-EF-53-B2-D6'    #12
    ,'9C-7B-EF-53-B6-48'    #13
    ,'9C-7B-EF-53-B4-D5'    #14
    ,'9C-7B-EF-53-B5-B9'    #15
    ,'9C-7B-EF-53-B4-B5'    #16
    ,'10-E7-C6-37-EB-10'    #17
    ,'10-E7-C6-37-EB-38'    #18
    ,'9C-7B-EF-53-B5-DB'    #19
    ,'9C-7B-EF-53-B5-C4'    #20
    ,None
    ,'9C-7B-EF-53-B5-7B'    #22 
    ,'9C-7B-EF-53-B4-ED'    #23
    ,'9C-7B-EF-53-B5-24'    #24
    ]
#,'9C-7B-EF-53-B6-01'    #21--unplugged
profileNames = [
    None                    #0
    ,None                   #1
    ,None                   #2
    ,'Lab-PC03'             #3
    ,'Lab-PC04'             #4
    ,'Lab-PC06'             #5
    ,'Lab-PC02'             #6
    ,'Lab-PC01'             #7
    ,'Lab-PC05'             #8
    ,'CLLB9'                #9
    ,'CLLB10'               #10
    ,'cllb11'               #11
    ,'cllb12'               #12
    ,'CLLB13'               #13
    ,'CLLB13'               #14
    ,'CLLB15'               #15
    ,'CLLB16'               #16
    ,'Lab-PC07'             #17
    ,'Lab-PC08'             #18
    ,'CLLB19'               #19
    ,'CLLB20'               #20
    ,None                   #21
    ,'CLLB22'               #22
    ,'CLLB23'               #23
    ,'CLLB24'               #24
    ]

username = 'Cliftonb'
password = 'Reddam2024'
localDistributionPath = 'C:/Users/Cliftonb/Documents/Python Projects/NetworkUtil/Distribution/'

def connectToNetworkComputer(host, username, password):
    unc = ''.join(['\\\\', host])
    try:
        win32wnet.WNetAddConnection2(0, None, unc, None, username, password)

    except Exception as err:
        if isinstance(err, win32wnet.error):
            # Disconnect previous connections if detected, and reconnect.
            if err[0] == 1219:
                win32wnet.WNetCancelConnection2(unc, 0, 0)
                return wnet_connect(host, username, password)
        raise err



def distributeFolderContents(folderPathSrc, folderPathDest):
    if os.path.exists(folderPathSrc) and os.path.exists(folderPathDest):

        #change the current directory to the folder to delete all files in
        os.chdir(folderPathSrc)

        #store the names of all the folders and files
        files = os.listdir()

        for file in files:

            #remove either a file
            if os.path.isfile(folderPathSrc + file):
                shutil.copy2(folderPathSrc + file, folderPathDest)

            #or a folder
            else:
                shutil.copytree(folderPathSrc + file, folderPathDest)

def deleteFolderContents(folderPath):

    #must be connected to network computer if path is a netword folder
    if os.path.exists(folderPath):

        #change the current directory to the folder to delete all files in
        os.chdir(folderPath)

        #store the names of all the folders and files
        files = os.listdir()

        print(str(files))
        print("\n\n" + folderPath + "\n\n")

        #response = input("Are you sure you want to delete the above files? y\\n")

        #if(response == "y"):
        if(True):

            #delete each file in the folder
            for file in files:

                #remove either a file
                if os.path.isfile(folderPath + file):
                    os.remove(folderPath + file)

                #or a folder
                else:
                    shutil.rmtree(folderPath + file)

    #folder path not found
    else:
        print("Error: " + folderPath + " coud not be reached")

def AdjustPrivilege(priv, enable=1):
    # Get the process token
    flags = TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY
    htoken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
    # Get the ID for the system shutdown privilege.
    idd = win32security.LookupPrivilegeValue(None, priv)
    # Now obtain the privilege for this process.
    # Create a list of the privileges to be added.
    if enable:
        newPrivileges = [(idd, SE_PRIVILEGE_ENABLED)]
    else:
        newPrivileges = [(idd, 0)]
    # and make the adjustment
    win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges)

def RebootServer(user=None,message='Rebooting', timeout=1, bForce=0, bReboot=0):
    AdjustPrivilege(SE_SHUTDOWN_NAME)
    try:
        win32api.InitiateSystemShutdown(user, message, timeout, bForce, bReboot)
    finally:
        # Now we remove the privilege we just added.
        AdjustPrivilege(SE_SHUTDOWN_NAME, 0)

def AbortReboot():
    AdjustPrivilege(SE_SHUTDOWN_NAME)
    try:
        win32api.AbortSystemShutdown(None)
    finally:
        AdjustPrivilege(SE_SHUTDOWN_NAME, 0)

def ClearDesktops():
    for i in range(len(hostNames)):
        if(hostNames[i] != None):
            mac = macAddresses[i]
            host = hostNames[i]
            profile = profileNames[i]
            networkDesktopPath = '//' + host + '/C$' + '/Users/' + profile + '/Desktop/'
            connectToNetworkComputer(host, username, password)
            deleteFolderContents(networkDesktopPath)

def ShutDownLab():
    for i in range(len(hostNames)):
        if(hostNames[i] != None):
            host = hostNames[i]
            try:
                RebootServer(host)
                print("Computer " + str(i) + " is shutting down ---- " + hostNames[i])
            except:
                print(hostNames[i] + " is unreachable")

def WakeUpLab():
    for i in range(len(macAddresses)):
        if(macAddresses[i] != None):
            try:
                send_magic_packet(macAddresses[i])
                print("Magic packet sent to computer: " + str(i) + " ---- " + macAddresses[i])
            except:
                print(hostName[i] + " magic packet not sent")


def DistributeToAll():
    for i in range(len(hostNames)):
        if(hostNames[i] != None):
            mac = macAddresses[i]
            host = hostNames[i]
            profile = profileNames[i]
            networkDesktopPath = '//' + host + '/C$' + '/Users/' + profile + '/Desktop/'
            connectToNetworkComputer(host, username, password)
            distributeFolderContents(localDistributionPath, networkDesktopPath)
#WakeUpLab()
#ShutDownLab()
#ClearDesktops()
#DistributeToAll()
