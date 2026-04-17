class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        // 1. Find middle
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // 2. Reverse second half
        ListNode* prev = NULL;
        ListNode* curr = slow->next;
        slow->next = NULL;  // break list

        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        // 3. Merge two halves
        ListNode* f = head;
        ListNode* b = prev;

        while (b) {
            ListNode* t1 = f->next;
            ListNode* t2 = b->next;

            f->next = b;
            b->next = t1;

            f = t1;
            b = t2;
        }
    }
};