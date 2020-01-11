import json

from centre import GetCenterFromDegrees

with open('json_path') as f:
    data = json.load(f)

# print(data)

# print(json.dumps(data, indent=4, sort_keys=True))
# print(type(data))
name = ""
type = ""
parent = ""
count = 0
mapping = {}
for value in data["features"]:
    coor = []
    for key, val in value.items():
        if key == "properties":
            for k, v in val.items():
                if k == "name":
                    name = v
                if k == "type":
                    type = v
                if k == "parent":
                    parent = v
        if key == "geometry":
            for k, v in val.items():
                if k == "coordinates":
                    count += len(v[0])
                    n = len(v[0])
                    for i in range(n):
                        coor.append(v[0][i])
    # print(name,type,parent,coor)
    lat = []
    lon = []
    for i in range(len(coor)):
        # print(coor[i][1])
        lat.append(coor[i][0])
        lon.append(coor[i][1])
        x, y = GetCenterFromDegrees(lat, lon)
        mapping[name] = [x, y]
# print(mapping)

# example for sorted dict by value in reverse order
# item = {"a" : 1,"b" : 2, "c"  :3}
# main_map = {k: v for k, v in sorted(item.items(), key=lambda item: item[1], reverse=True)}
# print(main_map)
