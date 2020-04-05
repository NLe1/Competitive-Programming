"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.



Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""

import itertools
class Solution:
    def expressiveWords(self, S: str, words: [str]) -> int:
        groupS = [[key, len(list(arr))] for key, arr in itertools.groupby(S)]
        count = 0
        for word in words:
            groupW = [[key, len(list(arr))] for key, arr in itertools.groupby(word)]
            if len(groupS) != len(groupW): continue
            isStreched = True
            for i, (letterS, freqS) in enumerate(groupS):
                letterW, freqW = groupW[i]
                if letterS != letterW or freqW > freqS or (freqS > freqW and freqS < 3):
                    isStreched = False
                    break
            if isStreched: count+=1

        return count

s = Solution()
print(s.expressiveWords("yyrrrrrjaappoooyybbbebbbbriiiiiyyynnnvvwtwwwwwooeeexxxxxkkkkkaaaaauuuu", ["yrrjjappooybbebriiyynvvwtwwoeexkauu","yrjjappooybbebrriyynnvwwttwoeexkaauu","yyrrjapoybbebriiynnvvwwtwoeexkaauu","yyrjappooyybebbrriyynnvwttwwooeexxkkau","yrjaapooybbebrriyynnvvwwttwooexkaau","yyrjjapooyybeebbrriiyynvwwttwoexxkau","yrrjaappoyybbeebbriynnvwwtwooexxkauu","yrrjjaapooybebriynnvvwwttwwooexkaau","yyrrjjappooyybebriiyynvvwttwoeexxkkaau","yrrjaappooybbebrriynvwwtwooeexkau","yyrjjaapooyybebrriiynvvwttwwooeexxkkaau","yyrrjappooyybbebriyynnvwwttwwoeexkkauu","yyrrjjaapoyybbeebriiyynnvwwtwwooexkkaau","yrjjaappooybbeebriiyynnvwwtwwoexkau","yrrjjappoyybbeebbrriiyynnvwttwwooexxkkaauu","yyrrjjapooyybbebbrriyynvwtwoexxkkaauu","yyrrjappoybebrriynvwwttwooeexkkauu","yrrjaappooybbeebriiyynnvvwwttwoexxkauu","yrrjapoybebbrriyynvvwwttwwoexkaau","yyrrjjapoybbeebbrriynnvwwtwwooexkaauu","yyrrjjapooyybbeebbriyynnvwtwwoexkaau","yrjjaapooyybebriynnvwwttwooeexxkkaauu","yyrjjaapooybbebbriiynvvwttwwoexxkkauu","yrjjaapooyybeebbriiyynvvwwttwoeexxkau","yrjjappooyybbebbrriiynvvwtwooeexxkkau","yyrrjjapoyybbebbrriiyynvwwtwwoexxkkaau","yrjjapooyybbeebriyynnvvwwtwoeexkkau","yrjapooyybebriiynnvvwwtwwooeexkauu","yyrjaapoyybbebbrriynnvwtwwoeexkauu","yrrjjappoybeebrriiynvvwwtwwoeexxkkaau","yrrjjapoybbeebrriiyynnvwwttwwoexxkaau","yyrrjaapoybeebrriiyynvwttwwooeexkauu","yyrjapoybbeebbrriyynnvvwwttwwooeexkaauu","yyrjappooybebrriiynvwtwwoeexxkaauu","yrrjjappooybebrriynnvvwttwooexkau","yrjjaapoybbeebbriiynnvvwttwooexkauu","yyrrjapooyybbeebriiyynnvvwtwwoeexxkaauu","yyrjjaappooybeebbrriiyynnvvwwtwwoeexkkau","yrrjappoyybbeebrriiynvvwwtwwoeexxkauu","yrjapooyybeebriiyynvvwttwwooeexxkaauu","yrjjappooyybbebbriiynnvwwtwooeexxkauu","yyrrjjappooybbeebbriyynnvwtwwooexxkkau","yyrrjjaapooybebriiyynvwwtwooeexxkkaauu","yrjjappooyybbeebbriiyynvwwtwwoeexkkau","yrrjjappooybbebrriiynvvwwtwwoexxkkaau","yrjjapooybebbriyynnvvwwttwwooeexxkkaau","yyrjjapoyybebbrriynvvwwttwoexkauu","yyrjappoyybebriiynnvvwttwwoexxkaauu","yyrjaapoybbeebriyynvvwwttwoeexkau","yrjjaappooyybbebbriiynnvvwtwooexxkau","yyrjjaappooyybbebrriiyynvvwttwooexkau","yrjjappoybbeebriyynnvvwwttwwooexxkkaau","yyrrjaapooybbebbriiyynnvwwtwwooexxkkaauu","yrrjaapooybbeebrriynnvvwwtwoeexxkkauu","yrjjaappooyybeebbrriyynnvvwttwwoexxkkauu","yrrjapooyybebriyynnvwwttwooeexkau","yyrjjaapooyybeebrriiynnvvwwttwoeexxkkau","yrjappooybebriyynnvvwttwwooeexkau","yrrjjaappoyybebbrriiyynvwwtwooexxkauu","yrjjappooybeebriynnvwwtwoeexkaauu","yrjaappoybbebbriiynnvwwttwooexxkaau","yyrrjappooyybeebbriiyynvwwttwwoexxkau","yyrjappoyybbeebrriynvwtwoeexkaau","yrrjjaapooybbeebbriyynvwwtwooeexkkaau","yrjapoybebbrriiynvwttwwoeexxkaau","yrjapooybebbrriiynnvwwtwwoexxkaau","yrrjjaappoybeebbriiyynvwwtwooexxkkaauu","yrjappooybeebrriynvwwtwooeexkaauu","yrrjaapooybeebbriiynvvwtwwoexxkkaauu","yyrrjaappooyybebbrriiyynvwwtwwooexxkkau","yyrjaappoybbeebriynnvvwwtwwooeexkaauu","yyrjaappooyybbebbriynvvwwttwwooexkauu","yrjappooybeebbrriiynnvwttwwooexkkau","yrrjjappooyybebbriiyynnvvwttwwoexkkau","yrrjjaapooybeebbriynnvvwwtwooexkaau","yyrjjappoybeebbrriiynnvwtwwoexkaauu","yyrjjaapoybbebbrriiyynnvvwtwwoexkaau","yyrrjjaappoyybbebbriyynvwwtwwooeexkkaau","yrrjjaappooybbebriiyynvvwttwwooexxkau","yyrjjaapoyybebriiynnvwtwwooeexkauu","yrrjjappoyybeebbriiyynnvwttwoexkkau","yrjjappoyybbebbrriynnvvwttwwooeexkkaauu","yyrjappooybeebrriiynnvwwttwwooexxkkaauu","yrrjaappoybbeebrriyynnvvwwtwwooeexxkaauu","yyrjaappooybeebbriiynvwttwoexxkkauu","yyrrjjapooyybbeebbrriyynvwttwwooeexxkkau","yrrjapoybbebbrriiynvwtwwoeexxkaau","yyrrjapoybbeebbriiyynnvvwttwooexkkauu","yyrjaapooyybebbrriiyynnvvwwtwooeexkkauu","yyrrjjaappoybbeebrriyynnvwwtwwoexkkaauu","yyrjappooybbeebrriiyynvwwttwwoexkkau","yyrjaapooyybebbriiyynnvvwwtwoeexkkaau","yyrrjjappoyybbeebbriiyynvwtwooexxkaauu","yrrjjaapoyybbeebriynvvwtwwoexxkaau","yyrrjjapoybbebbrriyynnvwwtwoeexxkkaau","yyrrjapooyybebrriiyynvwttwwooeexxkkauu","yrjappooyybebriiynnvwwtwoeexkkaauu","yrjjaapooyybeebriiynvwtwooexkauu","yyrrjjapoybeebbrriiynnvwttwwoexkaau","yyrrjaappoyybebbrriiyynvwwtwooeexkaau"]))