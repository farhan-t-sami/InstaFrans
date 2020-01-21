with open('Following.txt', "r") as x:
    following = (x.read().split('\n'))
with open ('Followers.txt', "r") as y:
    followers = (y.read().split('\n'))

trash = ['Follow', 'Following', 'Requested', 'Close', 'Followers', '', ' ']

for x in range(len(following)):
    if 'profile picture' in following[x]:following[x] = ':'

following = [x for x in following if x not in trash]
following = ' '.join(following)
following = following.split(' : ')
del following[0]

for x in range(len(followers)):
    if 'profile picture' in followers[x]:followers[x] = ':'

followers = [x for x in followers if x not in trash]
followers = ' '.join(followers)
followers = followers.split(' : ')
del followers[0]

suckers = set(following) - set(followers)

#for x in range(len(following)):
    #print (x+1, following[x])
#print(len(following))

#for y in range(len(followers)):
    #print (y+1, followers[y])
#print(len(followers))
n=1

print(len(suckers), "accounts to be unfollowed:\n")
for z in suckers:
    print (n, z)
    n+=1

