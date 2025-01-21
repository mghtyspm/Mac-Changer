## Features  
- Easy-to-use command-line interface.  
- Allows users to specify the network interface and desired MAC address.  
- Verifies current and updated MAC addresses to ensure successful changes.  

## Usage  
Run the script using Python with the following options:  
- `-i` or `--interface`: Specify the network interface (e.g., wlan0).  
- `-m` or `--mac`: Provide the new MAC address (e.g., 12:34:56:78:90:12).  

Example:  
```bash
python mac_changer.py -i wlan0 -m 12:34:56:78:90:12
