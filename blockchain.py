genesis_block = {
    'previout_hash': '', 
    'index': 0, 
    'transactions':[]
}
blockchain = []
open_transactions = []
owner = 'Max'

def hash_block(block):
    return '-'.join(str([block[key] for key in block]))

def get_last_blockchain_value():
    """ Returns the last value of the current block chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    tx_receipient = input('Enter the receipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_receipient, tx_amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def add_transaction(recipient, sender = owner, amount = 1.0):
    transaction = { 
        'sender': sender, 
        'receipient': recipient, 
        'amount': amount 
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = { 
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': open_transactions
    }
    blockchain.append(block)


waiting_for_input = True

while waiting_for_input:
    # Output the blockchain list to the console
    print('Please choose')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1': 
        tx_data = get_transaction_value()
        receipient, amount = tx_data
        add_transaction(receipient, amount = amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                 'previout_hash': '', 
                 'index': 0, 
                 'transactions':[{'sender': 'Chris', 'receipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print('Input invalid')
    if not verify_chain():
        print('Invalid blockchain')
        break

print('Done!')



