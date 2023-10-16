def MLPOP(client, list_key, number):
    transaction = client.pipeline(transaction=True)
    for i in range(number):
        transaction.lpop(list_key)
    return transaction.execute()

