from hashlib import sha256
import time


def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(BlockNumber, Transactions, PreviousHash, Prefix_Zero):
    MAX_NONCE = 100000000
    Prefix_str = '0' * Prefix_Zero

    for Nonce in range(MAX_NONCE):
        text = str(BlockNumber) + Transactions + PreviousHash + str(Nonce)
        newHash = SHA256(text)
        if newHash.startswith(Prefix_str):
            print("Yay! Successfully mined Bitcoins with Nonce value ", Nonce)
            return newHash

    raise BaseException("Couldn't find correct hash after trying {} times".format(MAX_NONCE))


if __name__ == '__main__':
    transactions = input("Enter a transaction details : ")
    Difficulty = 4

    while True:
        Block_number = input("Enter a block number : ")
        if not Block_number.isnumeric():
            print("Invalid input, Enter again ")
            print()
        else:
            break

    Block_number = int(Block_number)
    Previous_hash = input("Enter a Previous hash : ")
    print()

    start = time.time()
    print("Start Mining")
    new_hash = mine(Block_number, transactions, Previous_hash, Difficulty)

    total_time = str(time.time() - start)
    print("End mining. Mining took {} seconds".format(total_time))

    print("Hash of created block - ", new_hash)
