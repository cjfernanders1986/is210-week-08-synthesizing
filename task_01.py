#!usr/bin/env python
# -*- coding: utf-8 -*-
"""color comparison"""

BASE = raw_input('Choose base: Seattle Grey or Manatee: ')
ACCENT = raw_input('''Choose accent: Ceramic Glaze, Culumbus Nimbus,
Platnium Mist, or Spartan Sage: ''')
HIGHLIGHT = raw_input('''Choose highlight: Bascally White, White, Off-White,
Paper White, Bone White, Just White, Fractal White, Not White: ''')
SELECTIONS = '{}, {}, {}'

print 'You selected: ' + SELECTIONS.format(BASE, ACCENT, HIGHLIGHT)
