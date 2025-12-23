# Influence Recommendation System - Solution Analysis

## Understanding the Problem

So basically we need to build a friend recommendation system. Given a userK, we want to recommend L users who aren't already friends with K. The tricky part is how to rank them.

The main idea is:
- We can't recommend people who are already friends
- People with more mutual friends should be ranked higher
- If two people have the same number of mutual friends, prefer the one with more total friends (more active)
- If still tied, go with smaller user ID

Also need to handle edge cases - what if there aren't enough people with mutual friends? Then we fill with strangers (no mutual friends), sorted by their friend count. And if we still don't have enough, pad with zeros.

## My Approach

I decided to use a graph representation with dictionaries and sets. Sets are good because checking if someone is a friend is O(1), and finding mutual friends is just a set intersection.

Here's what I did:

1. **Build the graph**: Read all the friendships and store them in a dict where each user maps to a set of their friends. Since friendships are bidirectional, I add both directions.

2. **Find candidates**: Go through all users except K, skip if they're already friends. For each candidate, calculate:
   - How many mutual friends they have with K (using set intersection)
   - Their total friend count

3. **Separate into groups**: Split candidates into two lists:
   - Those with mutual friends (> 0)
   - Those without mutual friends (strangers)

4. **Sort each group**:
   - Group 1: Sort by mutual count (desc), then friend count (desc), then user ID (asc)
   - Group 2: Sort by friend count (desc), then user ID (asc)

5. **Build result**: Take L users from group 1 first, then fill from group 2 if needed, pad with zeros if still not enough

## Complexity

**Time**: 
- Building graph: O(M) where M is number of friendships
- Processing candidates: O(N * D) where N is users and D is average degree. For each candidate we do a set intersection which is O(min(friends of K, friends of candidate))
- Sorting: O(C log C) where C is number of candidates
- Overall: O(M + N*D + C log C), which in worst case is O(M + N²)

**Space**:
- Graph: O(M) - each edge stored twice
- Candidate lists: O(N)
- Total: O(M + N)

## Example

Input:
```
6 8 1 2
1 2
1 3
2 4
3 4
4 5
5 6
2 5
3 6
```

User 1's friends: {2, 3}
Non-friends to consider: {4, 5, 6}

- User 4: friends {2, 3, 5}, mutual with 1 = {2, 3} = 2 mutual friends
- User 5: friends {2, 4, 6}, mutual with 1 = {2} = 1 mutual friend  
- User 6: friends {3, 5}, mutual with 1 = {3} = 1 mutual friend

Sorting:
- User 4 has 2 mutual friends (highest) → rank 1
- User 5 and 6 both have 1 mutual friend, but user 5 has 3 total friends vs user 6's 2 → user 5 wins
- So result is [4, 5]

## Thoughts

This was a good problem to practice graph algorithms. The key insight was using sets for efficient mutual friend calculation - the & operator makes it really clean.

I also learned that separating the candidates into two groups makes the sorting logic much clearer. Trying to sort everything together would have been messy.

One thing I had to be careful about was the edge case where we need to pad with zeros. Almost forgot that part initially!

Overall I think the solution is pretty efficient. The set operations are fast, and the sorting is standard. Could maybe optimize further but for the given constraints (N ≤ 1024, M ≤ 10240) this should be fine.

