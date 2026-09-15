def verify_card_number(number: str) -> str:
    nums = [int(n) for n in list(number) if n in '1234567890']
    for i in range(len(nums) - 2, -1, -2):
        nums[i] *= 2
    total = sum(n - 9 if n > 9 else n for n in nums)

    return 'VALID!' if total % 10 == 0 else 'INVALID!'
