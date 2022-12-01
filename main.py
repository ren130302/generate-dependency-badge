def _dependency(line):

    if not line.count(" ") <= settings["level"]:
        return None

    if line.count(":") != 4:
        return

    for split in line.split(" ") :
        
        if split.find(":"):
            line = split.split(":")

    dependency = {
        "groupId":line[0],
        "artifactId":line[1],
        "packaging":line[2],
        "version":line[3],
        "goal":line[4].replace("\n", "")
    }

    return dependency

def _dependencies():
    
    dependencies = {}

    with open(settings["mavenTreeFilename"], encoding="utf8") as file:
        
        for line in file.readlines():
            dependency = _dependency(line)
            
            if dependency is not None:
                groupId = dependency.pop("groupId")
                etc = dependency
                
                dependencies.setdefault(groupId, [])
                dependencies[groupId].append(etc)
    
    return dependencies

def _badge(key, value, color):
    key = key.replace("-", "--")
    value = value.replace("-", "--")
    return f"![](https://img.shields.io/badge/{key}-{value}-{color})\n"

def __badge_dependencies():
    badge = []
    
    for k,v in _dependencies().items():
        for dependency in v:
            badge.append(_badge(dependency.get("artifactId"), dependency.get("version"), "infomation")) 
    
    return badge
    
def start():
    txt = []
    
    with open("README.md","r", encoding="utf8") as readme:
        txt = readme.readlines()
    
    idx = 0
    
    startIdx = 0
    endIdx = len(txt)
    startDepIdx = -1
    endDepIdx = -1

    for line in txt:   
        if line.startswith(settings["start_dependecies"]):
            startDepIdx = idx + 1
        if line.startswith(settings["end_dependecies"]):
            endDepIdx = idx
        
        idx += 1
    
    if startDepIdx == -1 or endDepIdx == -1:
        raise Exception("Need commentout dependencies")
    
    temp1 = txt[startIdx:startDepIdx]
    temp2 = __badge_dependencies()
    temp3 = txt[endDepIdx:endIdx]
    
    txt = temp1 + temp2 + temp3
    
    with open("README.md","w", encoding="utf8") as readme:
        readme.writelines(txt)
settings = {
    "mavenTreeFilename":"/home/runner/work/ASAP/ASAP/mvn_dependency_tree.txt",
    "start_dependecies":"<!-- start dependencies -->",
    "end_dependecies":"<!-- end dependencies -->",
    "level": 2
}

start()
