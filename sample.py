import streamlit as st
import numpy as np

def main():
    st.title('Random Number Generator')
    
    # Generate a random number between 1 and 100
    random_number = np.random.randint(1, 101)
    
    st.write(f'Random Number: {random_number}')
    
if __name__ == '__main__':
    main()
