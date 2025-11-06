from ft_filter import ft_filter
import sys


def main():
    try : 
        assert len(sys.argv) == 3 , "The argument are bad"
        
        s = sys.argv[1]
        n = sys.argv[2]
        
        assert isinstance(s, str) and n.isdigit, "The argument are bad"
        
        n = int(n)
        
        """split string into words"""
        words = s.split()
        
        result = ft_filter(lambda word: len(word) > n, words)
        
        print(result)
    except AssertionError as ae :
        print(f"AssertError: {ae}")

if __name__ == "__main__":
    main()