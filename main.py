from web3 import Web3
import matplotlib.pyplot as plt
import pyfiglet
from termcolor import cprint
import time
import numpy as np

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/b4f02cc6b04943a69dc4f25ee3fa3aaf"))
cprint(pyfiglet.figlet_format("Blockchain Analysis", font="digital"), "cyan")

cprint("Gathering data for the day until you click CTRL+C")
cprint("wait for 5-10 minutes+", "green")
data = []
stop = True
y = []
i = 5

while stop:
	try:
		y.append(i)
		data.append(web3.eth.block_number)
		time.sleep(5)
		i += 5
		
	except KeyboardInterrupt:
		stop = False
		break

plt.scatter(data, y)
plt.xlabel('Block numbers')
plt.ylabel('seconds')
plt.title('ETH Block number analysis')
 
plt.show()
