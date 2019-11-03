/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        List<ListNode> ctn = new ArrayList<ListNode>();
        ListNode cur = head;

        //keeping all the instances
        while(cur != null){
            ctn.add(cur);
            cur = cur.next;
        }

        if(n == ctn.size()){
            if(ctn.size() == 1){
                return null;
            }
            return ctn.get(1);
        }
        if(n == 1) {
            ctn.get(ctn.size() - 2).next = null;
            return head;
        }

        int index = ctn.size() - n;
        ctn.get(index - 1).next = ctn.get(index + 1);
        ctn.get(index).next = null;
        return head;

    }
}