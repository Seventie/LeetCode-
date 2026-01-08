class Node {
public:
    int val;
    Node* next;
    Node() : val(0), next(nullptr) {}
    Node(int val) : val(val), next(nullptr) {}
    Node(int val, Node* next) : val(val), next(next) {}
};

class MyLinkedList {
public:
    Node* head;

    MyLinkedList() {
        head = nullptr;
    }

    int get(int index) {
        int c = 0;
        Node* a = head;
        while (a && c != index) {
            a = a->next;
            c++;
        }
        if (!a) return -1;
        return a->val;
    }

    void addAtHead(int val) {
        Node* add = new Node(val);
        add->next = head;
        head = add;
    }

    void addAtTail(int val) {
        if (!head) {
            addAtHead(val);
            return;
        }
        Node* add = new Node(val);
        Node* iter = head;
        while (iter->next) {
            iter = iter->next;
        }
        iter->next = add;
    }

    void addAtIndex(int index, int val) {
        if (index < 0) return;

        if (index == 0) {
            addAtHead(val);
            return;
        }

        Node* curr = head;
        int i = 0;

        while (curr && i < index - 1) {
            curr = curr->next;
            i++;
        }

        if (!curr) return;

        Node* node = new Node(val);
        node->next = curr->next;
        curr->next = node;
    }

    void deleteAtIndex(int index) {
        if (!head || index < 0) return;

        if (index == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }

        Node* curr = head;
        int i = 0;

        while (curr->next && i < index - 1) {
            curr = curr->next;
            i++;
        }

        if (!curr->next) return;

        Node* del = curr->next;
        curr->next = del->next;
        delete del;
    }
};
