/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
            if(head == null) return true;
	        if(head.next == null) return true;

	        ListNode cur = head;
	        ArrayList<Integer> nodeStr = new ArrayList<Integer>();
	        while(cur != null){
	            nodeStr.add(cur.val);
	            cur = cur.next;
	        }

	        ArrayList<Integer> copyList = (ArrayList<Integer>) nodeStr.clone();
	        System.out.println(copyList);
	        Collections.reverse(nodeStr);
	        System.out.println(nodeStr);

	        if(copyList.equals( nodeStr)){
	            return true;
	        }else {
	            return false;
	        }
	    }

}