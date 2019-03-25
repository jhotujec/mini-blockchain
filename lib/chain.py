from lib.block import Block


class Chain:
    MINE_DIFFICULTY = 5

    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        assert isinstance(block, Block)
        block.mine_block(self.MINE_DIFFICULTY)
        self.blocks.append(block)

    def validate_chain(self):
        for (i, block) in enumerate(self.blocks):
            if block.hash != block.calculate_hash():
                return False
            if len(self.blocks) and i:
                if block.prev_hash != self.blocks[i - 1].hash:
                    return False
            if not block.hash.startswith(self.MINE_DIFFICULTY * "0"):
                return False
        return True

    def present(self):
        data = []
        exec_time = 0

        for block in self.blocks:
            data.append({
                'hash': block.hash,
                'nonce': block.nonce,
                'data': block.data,
                'timestamp': block.timestamp,
                'execution_time': block.execution_time
            })
            exec_time += block.execution_time

        return {
            'blocks': data,
            'is_valid': self.validate_chain(),
            'difficulty': self.MINE_DIFFICULTY,
            'avg_exec_time': (exec_time/len(self.blocks)),
            'full_exec_time': exec_time
        }