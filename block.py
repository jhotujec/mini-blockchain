import _hashlib
import binascii

from Crypto import Random
from Crypto.PublicKey import RSA

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


class BlockChain:
    def __init__(self):
        self.ledger = []

    def add_block(self, block):
        assert isinstance(block, Block)
        self.ledger.append(block)

    def list_blocks(self):
        return self.ledger


class Wallet:
    def __init__(self):
        random_generator = Random.new().read

        self.private_key = RSA.generate(1024, random_generator)
        self.public_key = self.private_key.publickey()

    @staticmethod
    def bin2hex(bin_str):
        return binascii.hexlify(bin_str)

    @staticmethod
    def hex2bin(hex_str):
        return binascii.unhexlify(hex_str)

    def encrypt_message(self, message):
        assert message
        result = self.public_key.encrypt(message, 32)[0]
        return Wallet.bin2hex(result)
