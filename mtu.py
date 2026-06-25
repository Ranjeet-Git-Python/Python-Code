log = "interface eth0 speed=1000 duplex=full mtu=1500"
data = log.split(" ")
cfg = {}
print(data)
for word in data:
    if "=" in word:
        data1 = word.split("=")
        if data1[0] == 'mtu':
            cfg[data1[0]] = data1[1]
print(cfg)