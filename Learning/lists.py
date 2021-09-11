coffee_order = ["Mary","Gary","Kelly","Melly"]
print(coffee_order[2])

fav_songs = ["Queen, Bohemien Rhapsofy","Black Sabbath, Iron Man","Britnesy Spears, Hit Me Bany","Phil Collins, In the Air Tonight"]
print(fav_songs[3])

fav_songs[0] =  "Chris Brown - No Guidance" # replacing the itme in a list by assigning a new value
print(fav_songs[0]) # returns the specified item in the list
print(len(fav_songs)) # returns number of items in a list or array
# .append is a method used to add items to a list
fav_songs.append("Michael Jackson, Thriller")
print(len(fav_songs))
# .pop is a method used to removes the last item in a list
fav_songs.pop()
print(fav_songs[-1])
print(len(fav_songs))
# .sort() .remove() .reverse() .count() .extend() etc...
# .sort() sorts the list asceding to a specified method
# .remove() removes the first instance of a specified item from a list
# .count() returns the number of times an item appears in a list
# .insert() 
# .clear() clears all items in a list
# .copy() copies the contents in a list
# .pop() removes the last item in a list
# .extend() can merge 2 or more lists
# .append() can modify a list by adding specified items
fav_songs.sort() # sorts items in list in ascending order
fav_songs.sort(reverse=True|False) # lists the items in a list in reverse order when specied true

fav_site = ["www.mangasail.com","www.youtube.com","www.netflix.com"]
fav_site.append("www.edx.com" and "www.coursera.com")
blocked_site = ["www.fakenews.com","www.boringcode.com","www.madeup.com"]
fav_site.extend(blocked_site)
print(fav_site)
fav_site.count("www.fakenews.com")
print(fav_site.count("www.fakenews.com"))
fav_site.remove(fav_site[-1])
print(fav_site)
fav_site.sort(reverse=True)
print(fav_site)
print(fav_site[-2],fav_site[-3]) #[-n] locates items specifed in the list index going backwards
print(fav_site[0:3]) # [n:n] is where : is used to locate items specified in the list from idex posintion n to n

coordinates=(1,2,3,4) # unlike lists [], tupples () cannot be reassgined or modified
print(coordinates[0]) # you can access elements in a tupple