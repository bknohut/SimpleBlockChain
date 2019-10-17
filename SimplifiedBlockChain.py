#### imports ####
import time
from djb2Hash import djb2
import MerkleTree
#################

class Header:
    def __init__(self):
        self.timestamp = "None"
        self.previousHash = "None"
        self.tx_root = None

    def InitializeBlockHeader(self, previousHash, tx_root):
        self.timestamp = time.time()
        self.previousHash = previousHash
        self.tx_root = tx_root

    def GetHeaderHash(self):
        result = str(self.timestamp) + str(self.previousHash)
        if self.tx_root is not None:
            return djb2(result + self.tx_root.data)
        return djb2(result)

    def DisplayHeader(self):
        result = "HEADER\nTimestamp: " + str(self.timestamp) + "\nPrevious Hash Value: " + str(self.previousHash) + \
               "\nTxRoot: "
        if self.tx_root is not None:
            return result + self.tx_root.data
        return result + "None"

class Block:
    def __init__(self):
        self.header = Header()
        self.transactions = []

    def AddTransactions(self, transactions):
        for transaction in transactions:
            self.transactions.append(transaction)

    def CreateBlock(self, previousHash):
        # create the tx root
        tx_root = self.BuildTxRoot()
        self.header.InitializeBlockHeader(previousHash, tx_root)

    def BuildTxRoot(self):
        tree = MerkleTree.MerkleTree()
        return tree.CreateTree(self.transactions)

    def DisplayBlock(self, index):
        result = "BLOCK " + str(index) + "\n" + self.header.DisplayHeader() + "\nTRANSACTIONS\n"
        for i in self.transactions:
            result += str(i) + " "
        return result

class BlockChain:
    def __init__(self):
        self.blocks = []
        self.InitializeBlockChain()

    def InitializeBlockChain(self):
        dummyHead = Block()
        dummyHead.header.previousHash = "-1"
        dummyHead.header.timestamp = time.time()
        self.blocks.append(dummyHead)

    def CreateBlock(self, block):
        previousHash = self.GetLastBlock().header.GetHeaderHash()
        block.CreateBlock(previousHash)
        self.blocks.append(block)

    def GetLastBlock(self):
        return self.blocks[-1]

    def DisplayChain(self):
        print("CHAIN")
        for i in range(len(self.blocks)):
            print("----------")
            print(self.blocks[i].DisplayBlock(i))


chain = BlockChain()
blocks = 6
t = ["T1", "T2"]
for i in range(1, blocks):
    block = Block()
    block.AddTransactions(t)
    chain.CreateBlock(block)
    print("Created Block" + str(i))
    print(block.DisplayBlock(i))
    print("Block " + str(i) + " Header Hash Value is: ")
    print(block.header.GetHeaderHash())
    t.append("T"+str(i+2))
    time.sleep(2)

print("\n\n\n")
chain.DisplayChain()

