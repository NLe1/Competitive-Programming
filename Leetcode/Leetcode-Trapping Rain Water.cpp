class Solution {
public:
    int trap(vector<int>& height) {
        int trap = 0;
        auto i = height.begin();

        while(i != height.end()){
            findPondAndCalculate(i, height.end() , trap);
        }

        return trap;
    }

void findPondAndCalculate(vector<int>::iterator &i, vector<int>::iterator end, int &trap){

    int anchor = *i;
    bool foundPuddle = false;
    int area = 0;
    i++; //copy and increment the iterator
    auto x = i;
    int maxElement = 0;
    vector<int> insideTerrain;

    while(x != end){
        if(*x >= anchor && insideTerrain.empty())
            return;

        if(*x >= anchor && !insideTerrain.empty()){
            foundPuddle = true;
            break;
        }

        if(*x < anchor){
            insideTerrain.push_back(*x);
            maxElement = (*x > maxElement) ? *x : maxElement;
        }
        x++;
        if(x == end && !insideTerrain.empty()){
            //backtrack to find the maxElement pointer
            x--;
            insideTerrain.pop_back();
            while(*x < maxElement){
                insideTerrain.pop_back();
                x--;
            }

            if(!insideTerrain.empty())
                foundPuddle =true;
            break;
        }
    }
    if(foundPuddle){
        area += min(anchor, *x) * insideTerrain.size();

        for(auto e : insideTerrain){
            area -= e;
        }

        i = x; //assign to new iterator if found the pond
        trap += area;
    }

    return;
}

};