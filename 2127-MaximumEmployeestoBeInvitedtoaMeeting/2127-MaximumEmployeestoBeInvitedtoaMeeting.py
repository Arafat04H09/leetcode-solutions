import collections


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        return max_invitations(favorite)

# Main.
def max_invitations(edges: list[int]) -> int:
    return max(get_maximum_circle_size(edges), get_maximum_chain_size(edges))


def get_maximum_circle_size(edges: list[int]) -> int:
    """Given a graph where each node has exactly one out-going edge, return the maximum circle size."""

    def get_maximum_circle_size_from(i: int) -> int:
        """Return the maximum circle size where it can be reached from node i or -1 if we reached to explored node first."""
        start = i  # The starting node index.
        curr = i  # The node index at each iteration.
        path = set()  # Store node indices on the current path.

        # Explore graph until we find the circle or explored node.
        while curr not in visited:
            visited.add(curr)
            path.add(curr)
            curr = edges[curr]

        # If we reached to one of the explored node before finding a new circle, abort.
        if curr not in path:  # but curr in visited.
            return -1

        # Otherwise, we have found a new circle, so determine its size.
        cursum = len(path)
        while start != curr:
            cursum -= 1
            start = edges[start]
        return cursum

    visited: set[int] = set()  # set of visited node indices.
    return max((get_maximum_circle_size_from(i) for i in range(len(edges))))


def get_maximum_chain_size(edges: list[int]) -> int:
    n = len(edges)  # The total number of nodes.

    def get_all_pair_circles() -> list[tuple[int, int]]:
        # First, find all pair (two nodes) circles.
        pairs: list[tuple[int, int]] = []
        on_pair = set()  # store node indices already on the pair list.
        for i in range(n):
            if edges[edges[i]] == i and i not in on_pair:
                pairs.append((i, edges[i]))
                on_pair.update((i, edges[i]))
        return pairs

    def get_maximum_arm_length_to(i: int, j: int) -> int:
        """Return the maximum arm length which comes into node i except from node j."""

        # Init dq with all nodes directly connected to i, expect j.
        NodeAndArmLength = collections.namedtuple(
            "NodeAndArmLength", ["node", "arm_length"]
        )
        dq: collections.deque[NodeAndArmLength] = collections.deque()
        for node in coming_to[i]:
            if node != j:
                dq.append(NodeAndArmLength(node, 1))

        # Determine the longest arm length.
        max_arm_length = 0
        while dq:
            node, arm_length = dq.popleft()
            max_arm_length = max(max_arm_length, arm_length)
            for next_node in coming_to[node]:
                dq.append(NodeAndArmLength(next_node, arm_length + 1))
        return max_arm_length

    # coming_to[i] is the set of node indices who has an edge towards i.
    coming_to: dict[int, set[int]] = collections.defaultdict(set)
    for i in range(n):
        coming_to[edges[i]].add(i)

    return sum(
        (
            get_maximum_arm_length_to(a, b)
            + get_maximum_arm_length_to(b, a)
            + 2  # + 2 for node a and b.
            for a, b in get_all_pair_circles()
        )
    )