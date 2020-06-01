# 024. Swap Nodes in Pairs

## Solution 1

Create a dummyHead, and then build the list iteratively.

* Time Complexity: O(N)

* Space Complexity: O(1)

### Pros

1. More convenient to hold the list.

### Cons

1. Creating a dummyHead might require many resource allocations

## Solution 2

Compared to sol 1, the solution does not need to create a new listNode, just build the list recursively.

* Time Complexity: O(N)

* Space Complexity: O(N)

### Pros

1. Doesn't need to create a new nodeList.

2. Elegant

### Cons

1. Could cause stack overflow if the length of the list is very long.

## Thinking

Sometimes, in industrial projects, it's not trivial to create a ListNode which might require many resource allocations or inaccessible dependencies (we need to mock them).

So ideally, we should pick up either the head of l1 or l2 as the head other than creating a new one, which however makes the initialization step tedious.

But during an interview, I would rather create a new ListNode as list holder, but communicate with the interviewer that I'm aware of the potential issue, and would improve it if the interviewer thinks this is a big deal.

But anyway, as long as we communicate this concerning properly with the interviewer, I don't think it's a big deal here.
