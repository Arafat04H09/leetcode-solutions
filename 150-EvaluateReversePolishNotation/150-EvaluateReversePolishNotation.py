class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        operations = "+-*/"
        for token in tokens:
            if token not in operations:
                st.append(int(token))
            else:
                a = st.pop()
                b = st.pop()
                if token == "+":
                    st.append(b + a)
                elif token == "-":
                    st.append(b - a)
                elif token == "*":
                    st.append(b * a)
                elif token == "/":
                    st.append(int(float(b) / a))
        
        return st[-1]