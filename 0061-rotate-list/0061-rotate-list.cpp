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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !k) return head;

        ListNode* tail = head;
        int len = 1;

        while(tail->next){
            len++;
            tail = tail->next;
        }

        if(k % len == 0) return head;
        k = k % len;

        // make circular
        tail->next = head;

        ListNode* pivot = tail;
        int cnt = len - k;

        while(cnt--){
            pivot = pivot->next;
        }

        head = pivot->next;
        pivot->next = nullptr;

        return head;
    }
};