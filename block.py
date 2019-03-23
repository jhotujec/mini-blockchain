import _hashlib

SEED = "mz8yPvgQpsWtf2SY"


class Block:
    def __init__(self, prev_block, data):
        self.prev_block = prev_block
        self.data = data
        self.signature = self._generate_signature()

    def __str__(self):
        return str(self.signature.hexdigest())

    def _generate_signature(self):
        if not self.prev_block:
            prev_signature = SEED
        else:
            prev_signature = self.prev_block.signature.hexdigest()

        signature = prev_signature + self.data
        return _hashlib.openssl_sha256(signature)


class BlockChain():
    def __init__(self):
        self.ledger = []

    def add_block(self, block):
        assert isinstance(block, Block)
        self.ledger.append(block)

    def list_blocks(self):
        return self.ledger
