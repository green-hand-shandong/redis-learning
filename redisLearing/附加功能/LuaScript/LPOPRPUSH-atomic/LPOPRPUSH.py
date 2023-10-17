def lpoprpush(client, source, target):
    script = """
        local source = KEYS[1]
        local target = KEYS[2]
        
        local item = redis.call("LPOP", source)
        if item~= false then 
            redis.call("RPUSH", target, item)
            return item
        end
    """
    return client.eval(script, 2, source, target)

