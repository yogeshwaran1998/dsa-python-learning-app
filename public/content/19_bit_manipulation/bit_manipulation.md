# Bit Manipulation - Theory Guide

## Bitwise Operations

| Operator | Description | Example |
|----------|-------------|---------|
| & | AND | 1 & 1 = 1 |
| \| | OR | 1 \| 0 = 1 |
| ^ | XOR | 1 ^ 0 = 1 |
| ~ | NOT | ~1 = -2 |
| << | Left shift | 1 << 2 = 4 |
| >> | Right shift | 4 >> 1 = 2 |

## Key Properties

- **XOR**: `a ^ a = 0`, `a ^ 0 = a`, `a ^ b ^ a = b`
- **AND with 1**: Extract bit
- **Left shift**: Multiply by 2^n
- **Right shift**: Divide by 2^n

## Common Tricks

1. **Check if power of 2**: `n & (n-1) == 0`
2. **Count bits**: `n &= (n-1)` loop
3. **Swap without temp**: `a ^= b; b ^= a; a ^= b`
4. **Get bit**: `(n >> i) & 1`
5. **Set bit**: `n | (1 << i)`
6. **Clear bit**: `n & ~(1 << i)`

## Interview Tips

1. Know all bitwise operations
2. Understand two's complement
3. Handle negative numbers carefully
4. Think about edge cases (overflow, etc.)
