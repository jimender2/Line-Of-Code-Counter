import requests


# Simple app that adds up how many lines of code someone has committed to Git

# Pull my projects from https://api.github.com/users/{user}/repos
user = 'jimender2'
data = requests.get('https://api.github.com/users/'+ user +'/repos').json()

repoList = []
for repo in data:
    repoList.append(str(repo['url'])+str('/stats/code_frequency'))


LinesOfCodeAdded = 0
LinesOfCodeRemoved = 0
for repo in repoList:
    results = requests.get(repo).json()

    for instance in results:
        LinesOfCodeAdded = LinesOfCodeAdded + instance[1]
        LinesOfCodeRemoved += instance[2]

print("LinesOfCodeAdded: ",LinesOfCodeAdded,", LinesOfCodeRemoved: ",LinesOfCodeAdded,"")