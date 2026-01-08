class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right)
            return head;

        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* ans = dummy;

        int n = 1;
        while (n < left) {
            dummy = dummy->next;
            n++;
        }

        ListNode* Left = dummy;
        ListNode* leftSave = dummy->next;
        ListNode* prev = nullptr;
        ListNode* curr = leftSave;

        int len = right - left + 1;
        while (len--) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        Left->next = prev;
        leftSave->next = curr;

        return ans->next;
    }
};
