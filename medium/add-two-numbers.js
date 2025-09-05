/**
 * LeetCode 2: Add Two Numbers
 * Difficulty: Medium
 * 
 * Problem: https://leetcode.com/problems/add-two-numbers/
 * 
 * Approach:
 * - Use linked list traversal
 * - Maintain carry while summing nodes
 * 
 * Time Complexity: O(max(m, n))
 * Space Complexity: O(max(m, n))
 */


//Definition for singly-linked list.
 function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let initial = new ListNode(0);
    let current = initial;
    let carryOver = 0;

    while( l1 != null || l2 != null || carryOver != 0 ){
        let x = l1 != null ? l1.val : 0;
        let y = l2 != null ? l2.val : 0;

        let sum = x + y + carryOver;
        carryOver = Math.floor(sum / 10);
        let digit = sum % 10;

        current.next = new ListNode(digit);
        current = current.next;

        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }

    return initial.next;

    
};
