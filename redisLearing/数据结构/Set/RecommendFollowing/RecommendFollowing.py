def following_key(user):
    return user + "::following"
def recommend_follow_key(user):
    return user + "::recommend_follow"

class RecommendFollowing:
    def __init__(self, client, user) -> None:
        self.client = client
        self.user   = user
    
    def calculate(self, seed_size): # 抽取 seed_size 个关注的人， 计算他们关注的并集 (注意，并集存储在redis数据库里面)
        user_following_key = following_key(self.user)
        seed_group = self.client.srandmember(user_following_key, seed_size) 
        seed_group_following_set = set()
        for someone in seed_group:
            seed_group_following_set.add(following_key(someone))
        return self.client.sunionstore(recommend_follow_key(self.user), *seed_group_following_set)
    
    def fetch_result(self, number): # 从并集中随机取出 number 个
        return self.client.srandmember(recommend_follow_key(self.user), number)
    
    def delete_result(self):
        self.client.delete(recommend_follow_key(self.user))