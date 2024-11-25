def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input()) 
        stream = input().split()
        freq = {}
        non_repeating = []
        result = []
        
        for char in stream:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
            if freq[char] == 1:
                non_repeating.append(char)

            while non_repeating and freq[non_repeating[0]] > 1:
                non_repeating.pop(0)
            
            if non_repeating:
                result.append(non_repeating[0])
            else:
                result.append("-1")
        results.append(" ".join(result))

    print("\n".join(results))

main()