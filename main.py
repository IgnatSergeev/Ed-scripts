import requests

def numberOfStars(system):#TODO
    return 7

with open("systems.txt", 'r') as systemsFile:
    for line in systemsFile:
        pass
    last_line = line
    lastPage = str(int(line) + 1)
    print(int(lastPage) - 1)

with requests.Session() as session:
    response = session.get("https://eddbapi.elitebgs.app/api/v4/systems?permit=false&page=" + lastPage)
    numOfPages = int(response.json()["pages"])
    for page in range(int(lastPage), numOfPages):
        print(page)
        response = session.get("https://eddbapi.elitebgs.app/api/v4/systems?permit=false&page=" + str(page))
        for system in response.json()["docs"]:
            numberOfStarsInCur = numberOfStars(system)
            if numberOfStarsInCur > 6:
                with open("systems.txt", 'a') as systemsFile:
                    systemsFile.write(system["name_lower"] + '\n')
        with open("systems.txt", 'a') as systemsFile:
            systemsFile.write(str(page) + '\n')


