import pickle
from random_loader import create_dataset as create_rand
from copious_loader import create_dataset as create_cop

random = "../data/pickle/random.pickle"
copious = "../data/pickle/copious.pickle"

rand_data = create_rand()
cop_data  = create_cop()

with (open(random, 'wb')) as f:
    pickle.dump(rand_data, f)
with (open(copious, 'wb')) as f:
    pickle.dump(cop_data, f)


loaded_obj = []
with (open(random)) as f:
    loaded_obj = pickle.load(f)

print(loaded_obj[0:5])


