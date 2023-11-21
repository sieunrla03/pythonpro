import pickle
print("Pickling lists.\n")
print("Unpickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
pickle_file = open("pickles1.dat", "wb")
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()

pickle_file = open("pickles1.dat", "rb")
variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)
pickle_file.close()
print (variety)
print (shape)
print (brand)

print("\nShelvinf lists.\n")
print("Retrievinf the lists from a shelved file: \n")
import shelve
pickle = shelve.open("pickles2.dat.db")
pickle["variety"] = ["sweet", "hot", "dill"]
pickle["shape"] = ["whole", "spear", "chip"]
pickle["brand"] = ["Claussen", "Heinz", "Vlassic"]
pickle.sync()

for key in pickle.keys():
        print (key, "-", pickle[key])
