#Task 1

class Pet():

    def __init__(self,name,species, hunger=5,happiness=5,energy=10):
        self.name = name
        self.species= species
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self):
        if self.hunger>=3:
            self.hunger -= 3
            self.energy+=1

        elif self.hunger<3:
            print(f'{self.name} is almost dying. Feed him!')

    def play(self):
        self.happiness+=2
        self.energy -= 2
        self.hunger += 1

    def sleep(self):
        self.energy = 10

    def status(self):
        print(f"{self.name} ({self.species}): hunger={self.hunger}, happiness={self.happiness}, energy={self.energy}")

pet = Pet("Rex", "Dog")
pet.status()
pet.play()
pet.feed()
pet.sleep()
pet.status()

#Task 2

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []          

    def add_song(self, song):
        self.songs.append(song)  

    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:     
                self.songs.remove(song)
                return
        print(f"No song titled '{title}' found.")

    def total_duration(self):
        total = sum(song.duration for song in self.songs)  
        print(f"{total // 60}m {total % 60}s")

    def shuffle(self):
        import random
        random.shuffle(self.songs)
        print("New order:")
        for song in self.songs:
            print(f"- {song.title}")

p = Playlist("Road Trip")
p.add_song(Song("Song A", "Artist X", 200))
p.add_song(Song("Song B", "Artist Y", 180))
p.total_duration()
p.shuffle()
p.remove_song("Song A")
print(len(p.songs))            




