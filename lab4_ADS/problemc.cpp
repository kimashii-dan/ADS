#include <iostream>
using namespace std;
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int val) {
    if (!root) return new Node(val);
    if (val < root->data)
        root->left = insert(root->left, val);
    else
        root->right = insert(root->right, val);
    return root;
}


Node* find(Node* root, int k) {
    if (!root || root->data == k)
        return root;
    if (k < root->data)
        return find(root->left, k);
    else
        return find(root->right, k);
}

void preorder(Node* root) {
    if (!root) return;
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

int main() {
    int n;
    cin >> n;
    int gifts[n];

    for (int i = 0; i < n; i++) {
        cin >> gifts[i];
    }

    int k;
    cin >> k;

    Node* root = nullptr;
    for (int i = 0; i < n; i++) {
        root = insert(root, gifts[i]);
    }

    Node* k_node = find(root, k);

    preorder(k_node);
    cout << endl;

    return 0;
}
