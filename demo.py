#!/usr/bin/env python3

import os

from pybullet_suncg.simulator import BulletSimulator
from pybullet_suncg.house import House

# NOTE: change suncg_dir to root directory of suncg data
suncg_dir = os.path.join(os.path.expanduser('~'), 'work', 'suncg')
sim = BulletSimulator(mode='gui', data_dir_base=suncg_dir, verbose=True)
house_id = 'd119e6e0bd567d923aea774c2a984bf0'
h = House(house_json=f'{suncg_dir}/house/{house_id}/house.json')
sim.add_house(h, no_walls=False, no_ceil=True, use_separate_walls=False, static=False)
sim.run()
