from redisCluster import RedisCluster

nodes = [{"host":"","port":""}]

cluster = RedisCluster(startup_nodes=nodes, decode_responses=True)

cluster.set("msg", "hello")
cluster.get("msg")

cluster.cluster_keyslot("msg")
cluster.cluster_get_keys_in_slot()


for cmd in dir(cluster):
    if cmd.startswith("cluster"):
       print(cmd)
# cluster
# cluster_addslots
# cluster_count_failure_report
# cluster_countkeysinslot
# cluster_delslots
# cluster_failover
# cluster_get_keys_in_slot
# cluster_info
# cluster_keyslot
# cluster_meet
# cluster_nodes
# cluster_replicate
# cluster_reset
# cluster_reset_all_nodes
# cluster_save_config
# cluster_set_config_epoch
# cluster_setslot