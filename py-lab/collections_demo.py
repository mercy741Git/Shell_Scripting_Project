servers = ["web-01", "web-02", "web-03"]     # LIST
config  = {"port": 8080, "tls": True}         # DICT
azs     = ("az-a", "az-b")                    # TUPLE (fixed)
seen    = {"web-01", "web-01", "web-02"}      # SET (dedups!)
print(servers[0])               # web-01  (index)
print(config["port"])           # 8080    (dict lookup)
for s in servers:               # loop the list
    print("checking", s)
print("unique servers:", seen)  # {'web-01', 'web-02'}
servers.append("web-04")        # lists are changeable
print(len(servers))             # 
print(azs[1])                   # az-a
#azs.append("az-c")                 # TUPLE is fixed, cannot append
#print(len(azs))