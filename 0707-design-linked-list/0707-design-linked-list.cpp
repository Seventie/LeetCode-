class Node {
public:
    int val;
    Node* next;
    Node(int val,Node* next = NULL){
        this->val = val;
        this->next = next;
    }   
};
class MyLinkedList {
public:
    Node* head;
    MyLinkedList() {
        head = NULL;
    }  
    int get(int index) {
        if(!head) return -1 ;
        if(index < 0) return -1; 
        
        Node* a = head ;
        int idx = 0 ; 
        
        while((a) && (idx != index)){
            a = a->next;
            idx++;
        }
        
        if(!a) return -1;
        return a->val;
    } 
    void addAtHead(int val) {
        if(!head){
            head = new Node(val);
        }
        else{
            Node* temp = head ;
            head = new Node(val,temp);
        }
    }
    void addAtTail(int val) {
        if(!head){
            head = new Node(val);
            return;   
        }
        Node* a = head ;
        while(a->next){
            a = a->next ;
        }
        a->next = new Node(val);
    }  
    void addAtIndex(int index, int val) {
        if(index < 0) return;  
        if(index == 0){
            addAtHead(val);
            return;
        }
        Node* a = head ;
        int idx = 0;  
        while((a) && (idx != index-1)){
            a = a->next;
            idx++;
        }
        if(!a) return; 
        Node* temp = a->next;
        a->next = new Node(val, temp);
    }
    
    void deleteAtIndex(int index) {
        if(!head || index < 0) return;
        if(index == 0){
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node* a = head;
        int idx = 0;
        while((a->next) && (idx != index-1)){
            a = a->next;
            idx++;
        }
        if(!(a->next)) return; 
        Node* temp = a->next;
        a->next = temp->next;
        delete temp;
    }
};
/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */