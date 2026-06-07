#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isValid(char* s) {
    int len = strlen(s);
    
    // An odd length string can never be validly matched
    if (len % 2 != 0) return false;

    // Allocate memory for the stack. 
    // In the worst case (e.g., "((((((", we will push at most len elements)
    char* stack = (char*)malloc(len * sizeof(char));
    int top = -1; // Index of the top element in the stack

    for (int i = 0; i < len; i++) {
        char current = s[i];

        // 1. If it's an opening bracket, push it onto the stack
        if (current == '(' || current == '[' || current == '{') {
            stack[++top] = current;
        } 
        // 2. If it's a closing bracket
        else {
            // If stack is empty, there is no matching opening bracket
            if (top == -1) {
                free(stack);
                return false;
            }

            char openBracket = stack[top--]; // Pop the top element

            // Check if the popped bracket matches the current closing bracket
            if ((current == ')' && openBracket != '(') ||
                (current == ']' && openBracket != '[') ||
                (current == '}' && openBracket != '{')) {
                free(stack);
                return false;
            }
        }
    }

    // If the stack is completely empty, all brackets found a match!
    bool result = (top == -1);
    free(stack);
    return result;
}