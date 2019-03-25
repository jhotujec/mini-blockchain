import datetime
import hashlib
import time


class Block:
    def __init__(self, data, prev_hash):
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = Block._get_timestamp()
        self.nonce = 0
        self.execution_time = time.time()
        self.hash = self.calculate_hash()

    def __str__(self):
        return "<Block {0} - {1}>".format(self.data, self.hash)

    @staticmethod
    def _get_timestamp():
        now = datetime.datetime.utcnow()
        return (now - datetime.datetime(1970, 1, 1)).total_seconds()

    @staticmethod
    def _hash_func(to_hash):
        """
        Generate a hash string using sha256 from input string.
        :param to_hash:
        :return:
        """
        return hashlib.sha256(to_hash).hexdigest()

    def calculate_hash(self):
        """
        Generate block hash signature
        :return:
        """
        to_hash = self.prev_hash + str(self.timestamp) + self.data + str(self.nonce)
        return Block._hash_func(to_hash)

    def mine_block(self, difficulty):
        while not self.hash.startswith("0" * difficulty):
            self.nonce += 1
            self.hash = self.calculate_hash()

        end = time.time()
        self.execution_time = end - self.execution_time
