/*
	Problem URL: https://leetcode.com/problems/valid-parentheses/description/
*/

import java.util.Stack;  

class Solution {
    public boolean isValid(String s) {

		HashMap<Character, Character> closingBrackets = new HashMap<Character, Character>();
		// Handling closing brackets.
		Stack <Character> stack = new Stack<Character>();
		closingBrackets.put(')', '(');
		closingBrackets.put('}', '{');
		closingBrackets.put(']', '[');
		// Loop over passed string.
		// if it's opening bracket push it to stack.
		for(int i =0; i < s.length(); i++){
			Character c = s.charAt(i);
			if(c == '[' || c == '(' || c == '{')
				stack.push(c);
			else{
				// if stack is empty and we push closing bracket it's invalid.
                if(stack.isEmpty())
                    return false;
				// pop each closing bracket if it's meet its opposite opening bracket.
				if(stack.peek() == closingBrackets.get(c))
					stack.pop();
				else
					return false;
			}
		}
		// after poping all elements stack must be empty if the passed bracket is valid.
        if(stack.isEmpty())
            return true;
        return false;
    }
}