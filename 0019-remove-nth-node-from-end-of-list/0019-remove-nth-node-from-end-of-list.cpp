/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len = 0;
        ListNode* a = head;
        while(a){
            len++;
            a = a->next;
        }
        if(n == len){
            ListNode* temp = head;
            head = head->next;
            delete temp;
            return head;
        }
        a = head;
        int idx = 0;
        while(idx != len - n - 1){
            idx++;
            a = a->next;
        }
        ListNode* del = a->next;
        a->next = a->next->next;
        delete del;
        return head;
    }
};