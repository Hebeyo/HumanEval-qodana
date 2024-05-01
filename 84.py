def solve(N):
    # Write your code here
    return bin(sum(int(i) for i in str(N)))[2:]
