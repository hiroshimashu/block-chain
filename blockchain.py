blockchain = []

def get_last_blockchain_value():
    """ Returns the last value of the current block chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input('Your transaction amount please: '))

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        return is_valid



# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)




while True:
    # Output the blockchain list to the console
    print('Please choose')
    print('1: Add a new transaction')
    print('2: Output the blockchaine blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1': 
        tx_amount = get_user_input()
        add_value(last_transaction = get_last_blockchain_value(),
                  transaction_amount = tx_amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else: 
        print('Input invalid')
    if not verify_chain():
        print('Invalid blockchain')
        break

print('Done!')



