import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        if avgFriendships > numUsers:
            print("Not enough people")
        else:
            ids=[]
            for userId in range(numUsers):
                self.addUser('generated')
                temp=round(random.gauss(avgFriendships,1))
                if temp<0:
                    temp=0
                ids.extend([self.lastID]*int(temp))


            random.shuffle(ids)
            # ids=ids[:avgFriendships*numUsers//2]
            
            friends={}
            while len(ids)>1:
                f1=ids.pop()
                f2=ids.pop()
                held=[]

                if not friends.get(f1):
                    friends[f1]=set()

                while f2==f1 and not f2 in friends.get(f1) and len(ids)>0:
                    held.append(f2)
                    f2=ids.pop()
                if not f2 in friends.get(f1):
                    ids.extend(held)
                    self.addFriendship(f1,f2)
                    friends.get(f1).add(f2)

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        toVisit=Queue()
        toVisit.push(userID)
        visited[userID]=set([userID])
        while toVisit.size>0:
            current = toVisit.pop()
            for friend in self.friendships[current]:
                if not visited.get(friend):
                    visited[friend]=visited.get(current).copy()
                    visited[friend].add(current)
                    visited[friend].add(friend)
                    toVisit.push(friend)

        return visited

class Queue():
    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None
    
    def push(self, data):
        if self.size>0:
            self.tail.next=Cell(data)
            self.tail=self.tail.next
        else:
            temp=Cell(data)
            self.tail=temp
            self.head=temp
        self.size+=1
    
    def pop(self):
        if not self.head:
            return None
        else:
            self.size-=1
            temp=self.head.data
            self.head=self.head.next
            return temp
    
    def size(self):
        return self.size



    
class Cell:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
