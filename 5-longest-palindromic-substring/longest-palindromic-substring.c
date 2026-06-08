#include <string.h>
#include <stdlib.h>

// Helper function to expand around a center and return the length of the palindrome
int expandAroundCenter(char* s, int left, int right, int len) {
    while (left >= 0 && right < len && s[left] == s[right]) {
        left--;
        right++;
    }
    // Returns the length of the palindrome found
    return right - left - 1;
}

char* longestPalindrome(char* s) {
    int len = strlen(s);
    if (len < 1) {
        char* empty = (char*)malloc(sizeof(char));
        empty[0] = '\0';
        return empty;
    }

    int start = 0; // Tracks the starting index of the longest palindrome
    int maxLen = 0; // Tracks its length

    for (int i = 0; i < len; i++) {
        // Case 1: Odd-length palindromes (e.g., "aba", center is 'b')
        int len1 = expandAroundCenter(s, i, i, len);
        
        // Case 2: Even-length palindromes (e.g., "abba", center is between 'b' and 'b')
        int len2 = expandAroundCenter(s, i, i + 1, len);
        
        // Get the maximum length between the two cases
        int currentLen = (len1 > len2) ? len1 : len2;

        // If we found a palindrome longer than our current record
        if (currentLen > maxLen) {
            maxLen = currentLen;
            // Calculate the new start position
            start = i - (currentLen - 1) / 2;
        }
    }

    // Allocate memory on the heap for the result string (+1 for null terminator)
    char* result = (char*)malloc((maxLen + 1) * sizeof(char));
    strncpy(result, s + start, maxLen);
    result[maxLen] = '\0'; // Manually null-terminate

    return result;
}