from redis import Redis
from WeekMonthYearCounter import UniqueCounterMerge

client = Redis(decode_responses=True)
ucm = UniqueCounterMerge(client, "ucm")
counters = [
    "unique_ip_counter::8-10",
    "unique_ip_counter::8-10",
    "unique_ip_counter::8-10",
    "unique_ip_counter::8-10",
    "unique_ip_counter::8-10",
    "unique_ip_counter::8-10",
    "unique_ip_counter::8-10"
]

ucm.merge("unique_ip_counter::week_33", *counters)
