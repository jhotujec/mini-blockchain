import pprint

from lib.block import Block
from lib.chain import Chain

pp = pprint.PrettyPrinter(indent=4)

bc = Chain()

# Generate genesis block
b0 = Block("Genesis block", "0")
bc.add_block(b0)

b1 = Block("first transaction", b0.hash)
bc.add_block(b1)

b2 = Block("second transaction", b1.hash)
bc.add_block(b2)

pp.pprint(bc.present())

hb = Block("first transaction - fake", b0.hash)
bc.blocks[1] = hb

pp.pprint(bc.present())