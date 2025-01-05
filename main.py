def countElements(self, nums: List[int]) -> int:
    n = Counter(nums)
    an = 0
    d = min(nums)
    p = max(nums)

    for i, s in n.items():
        if i != p and i != d:
            an += s

    return an
