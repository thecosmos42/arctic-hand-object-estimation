import pickle, numpy as np
with open('MANO_RIGHT.pkl', 'rb') as f:
    mano = pickle.load(f, encoding='latin1')
np.save('mano_faces.npy', mano['f'].astype(np.int32))
