import os

def fullpath(filename):
    path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(path, filename)

def readfile(filename):
    with open(fullpath(filename), "r") as file:
        contents = file.read().split('\n\n')
        return "".join(contents[3:]).split('\n')

def filtered(filterlist):
    return [element[:-18] for element in filterlist if 'profile picture' in element]

def writefile(filename, value):
    with open(fullpath(filename), "w") as file:
        file.write("Unfollowers: \n\n")
        for v in value: 
            file.write(v)
            file.write("\n")

def instaPy():
    following = filtered(readfile('following.txt'))
    followers = filtered(readfile('followers.txt'))
    unfollowers = set(following) - set(followers)
    return unfollowers

if __name__ == "__main__":
    writefile("unfollowers.txt", instaPy())