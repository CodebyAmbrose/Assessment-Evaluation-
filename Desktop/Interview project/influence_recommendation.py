# friend recommendation thing
# gotta find top L users for user K

def solve():
    # parse input
    line = input().split()
    N = int(line[0])
    M = int(line[1])
    K = int(line[2])
    L = int(line[3])
    
    # build graph using dict with sets (sets are fast for lookups)
    graph = {}
    for i in range(1, N + 1):
        graph[i] = set()
    
    # read friendships
    for i in range(M):
        data = input().split()
        a = int(data[0])
        b = int(data[1])
        graph[a].add(b)
        graph[b].add(a)  # need both directions
    
    # get K's friends
    k_friends = graph[K]
    
    # split into two groups - ones with mutual friends and ones without
    with_mutual = []
    without_mutual = []
    
    # check each user
    for user in range(1, N + 1):
        if user == K:
            continue  # skip ourselves
        if user in k_friends:
            continue  # already friends so skip
        
        # calc mutual friends using set intersection
        user_friends = graph[user]
        mutual = k_friends & user_friends  # pretty neat trick
        mutual_count = len(mutual)
        total_friends = len(user_friends)
        
        if mutual_count > 0:
            with_mutual.append((user, mutual_count, total_friends))
        else:
            without_mutual.append((user, total_friends))
    
    # sort: mutual count desc, friend count desc, id asc
    with_mutual.sort(key=lambda x: (-x[1], -x[2], x[0]))
    
    # sort strangers: friend count desc then id
    without_mutual.sort(key=lambda x: (-x[1], x[0]))
    
    result = []
    
    # take from mutual friends first
    for item in with_mutual:
        result.append(item[0])
        if len(result) == L:
            break
    
    # if we need more grab from strangers
    if len(result) < L:
        for item in without_mutual:
            result.append(item[0])
            if len(result) == L:
                break
    
    # fill zeros if still not enough
    while len(result) < L:
        result.append(0)
    
    # output
    print(' '.join(str(x) for x in result))


if __name__ == '__main__':
    solve()

