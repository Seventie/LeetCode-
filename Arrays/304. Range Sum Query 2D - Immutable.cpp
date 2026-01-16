class NumMatrix {
public:
    vector<vector<int>> store;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        store.resize(m + 1, vector<int>(n + 1, 0));
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                store[i][j] = matrix[i-1][j-1] - store[i-1][j-1] +store[i][j-1] + store[i-1][j];
            }
        }
    }
    int sumRegion(int row1, int col1, int row2, int col2) {
        return store[row2+1][col2+1] - store[row2+1][col1] - store[row1][col2+1] + store[row1][col1];
    }
};
