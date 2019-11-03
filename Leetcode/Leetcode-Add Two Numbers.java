import java.math.*;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        while(l1 != null){
            sb1.append(l1.val + "");
            if(l1.next != null)
                l1 = l1.next;
            else
                break;
        }
        while(l2 != null){
            sb2.append(l2.val + "");
            if(l2.next != null)
                l2 = l2.next;
            else
                break;
        }
        BigInteger result = new BigInteger(new BigInteger(sb1.reverse().toString()).add(new BigInteger(sb2.reverse().toString())).toString());
        sb1 = new StringBuilder(result.toString());
        String resultString= sb1.reverse().toString();
        ListNode node = new ListNode(Integer.parseInt(resultString.charAt(0) + ""));
        ListNode cursor = node;
        for(int i = 1;i<resultString.length();i++){
            cursor.next = new ListNode(Integer.parseInt(resultString.charAt(i) + ""));
            cursor = cursor.next;
        }
        return node;
    }
}