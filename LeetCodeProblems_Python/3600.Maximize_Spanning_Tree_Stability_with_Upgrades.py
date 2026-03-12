class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        must_edges = []
        opt_edges = []
        for u, v, s, m in edges:
            if m == 1:
                must_edges.append((u, v, s))
            else:
                opt_edges.append((u, v, s))

        # Union-Find with path compression + union by rank
        def make_uf():
            return list(range(n)), [0] * n

        def find(par, x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def unite(par, rnk, x, y):
            px, py = find(par, x), find(par, y)
            if px == py:
                return False
            if rnk[px] < rnk[py]:
                px, py = py, px
            par[py] = px
            if rnk[px] == rnk[py]:
                rnk[px] += 1
            return True

        # Check must-edges form a forest (no cycles)
        par, rnk = make_uf()
        for u, v, s in must_edges:
            if not unite(par, rnk, u, v):
                return -1

        if not edges:
            return 0 if n <= 1 else -1

        max_s = max(s for u, v, s, m in edges)

        def feasible(t):
            # All must-edges must meet threshold
            for u, v, s in must_edges:
                if s < t:
                    return False

            par, rnk = make_uf()
            for u, v, s in must_edges:
                unite(par, rnk, u, v)

            # Heap: (needs_upgrade, u, v)
            # 0 = free edge (no upgrade), 1 = needs upgrade
            # Min-heap ensures free edges are used first
            heap = []
            for u, v, s in opt_edges:
                if s >= t:
                    heapq.heappush(heap, (0, u, v))
                elif 2 * s >= t:
                    heapq.heappush(heap, (1, u, v))

            upgrades = 0
            while heap:
                need_up, u, v = heapq.heappop(heap)
                if find(par, u) != find(par, v):
                    unite(par, rnk, u, v)
                    upgrades += need_up

            # Check all nodes connected and within budget
            root = find(par, 0)
            for i in range(1, n):
                if find(par, i) != root:
                    return False
            return upgrades <= k

        lo, hi, ans = 1, 2 * max_s, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans