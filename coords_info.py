import numpy as np
d = np.load('outputs/processed_verts/seqs/s01/capsulemachine_use_01.npy', allow_pickle=True).item()
wc = d['world_coord']
print("Keys in world_coord:", wc.keys())
for k in wc:
    val = wc[k]
    print(f"{k}: type={type(val)}, shape={np.shape(val)}")
    if hasattr(val, '__len__'):
        print(f"   first element shape: {np.shape(val[0])}")
