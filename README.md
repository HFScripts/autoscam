# ScamScan
Grab untrustworthy sites and sites under 10% get directory scanned

## This script is design to grab a number of domains from scamdoc using scraping and run a directory scan against them if they are still live. In hopes to find exposing information.
I recommend this wordlist for quick testing:
https://gist.github.com/htkcodes/f11eea99bd125064580d21725ed36e73

## Requirements
In order to use this script, you will need to have the following Python libraries installed:

re
requests
BeautifulSoup
You will also need to have the dirsearch tool installed on your system, which can be downloaded from the following GitHub repository: https://github.com/maurosoria/dirsearch

Usage
To use the script, simply copy and paste the code into a Python file and specify the necessary parameters in the wordlist_file, start_number, and end_number variables at the top of the script.

The wordlist_file variable should be set to the path of a wordlist file that dirsearch can use for directory scanning.

The start_number and end_number variables specify the range of ScamDoc document numbers to query. The script will query the API for each integer between start_number and end_number, inclusive.

Once you have set the necessary parameters, simply run the script and wait for it to complete.

Note that the script uses the User-Agent header to make HTTP requests, so you may want to customize this header to match your own user agent string.

Disclaimer
This script is provided for educational and informational purposes only. Use it at your own risk and responsibility. The author of this script is not responsible for any damages or legal issues arising from its use.

License
This script is licensed under the MIT License. See the LICENSE file for more information.
