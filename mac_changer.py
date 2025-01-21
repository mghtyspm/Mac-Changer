import subprocess
import optparse
import re

# Get User Arguments
def user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Use this option to choose the interface to change MAC e.g. wlan0")
    parser.add_option("-m", "--mac", dest="mach_Addy",
                      help="Use this option to change the MAC Address of selected interface e.g. 12:34:56:78:90:12")
    (options, arguments) = parser.parse_args()
    # Check for missing inputs
    if not options.interface:
        parser.error("[-] Please specify the interface to use; Use --help for more information.")
    if not options.mach_Addy:
        parser.error("[-] Please specify a new MAC Address to use; Use --help for more information.")
    return options

# Mac_changer function
def mac_changer(interface, mach_addy):
    print("[+] Changing MAC ADDRESS for " + interface + " to " + mach_addy)

    # disable interface
    subprocess.call(["ifconfig", interface, "down"])
    # Manually input the desired MAC Addr.
    subprocess.call(["ifconfig", interface, "hw", "ether", mach_addy])
    # Enable Interface
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_add_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_add_search_result:
        return mac_add_search_result.group(0)
    else:
        print("Could not read MAC Address")

options = user_input()
current_mac = get_current_mac(options.interface)

if current_mac:
    print("Current MAC ADDRESS= " + str(current_mac))
    mac_changer(options.interface, options.mach_Addy)
    updated_mac = get_current_mac(options.interface)

    if updated_mac and updated_mac.lower() == options.mach_Addy.lower():
        print("[+] MAC ADDRESS was successfully changed to: " + updated_mac)
    else:
        print("[-] MAC ADDRESS did not get changed.")
else:
    print("[-] Exiting: Could not fetch current MAC ADDRESS.")
