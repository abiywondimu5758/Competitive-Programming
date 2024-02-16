/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

// Iterative Solution
var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode(-1);  
    let tail = dummy;
    current1 = list1
    current2 = list2
    while(current1 != null && current2 != null){
        if(current1.val <= current2.val){
            tail.next = current1
            current1 = current1.next
        }
        else{
            tail.next = current2
            current2 = current2.next  
        }
        tail = tail.next
    }
    if(current1 != null) {
        tail.next = current1;
    } else {
        tail.next = current2;
    }
    return dummy.next;
};

// Recursive Solution
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if (list1 == null){
        return list2
    }
    if (list2 == null){
        return list1
    }

    if(list1.val < list2.val){
        list1.next = mergeTwoLists(list1.next,list2)
        return list1
    }
    else{
        list2.next = mergeTwoLists(list1,list2.next)
        return list2
    }
};
