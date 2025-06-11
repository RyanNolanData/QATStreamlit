import streamlit as st

st.set_page_config(
    page_title="Word Pattern Tools",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Word Pattern Tools")
st.markdown("---")

st.markdown("""
## Welcome to Word Pattern Tools

This application provides two powerful word pattern matching tools:

### 📝 **Word Pattern Matcher**
- Advanced pattern matching with variables and equations
- Support for anagrams, reverse patterns, and composite queries
- Regular expression-like patterns with vowel (@) and consonant (#) wildcards
- Variable definitions with length constraints

### 🔍 **QAT Search** 
- Quick and efficient pattern searching
- Variable-based word combinations
- Simple syntax for complex queries
- Fast results for large wordlists

---

**👈 Use the sidebar to navigate between the tools!**
""")

st.markdown("---")
st.markdown("### Quick Start Guide")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Word Pattern Matcher Examples:**
    ```
    # Simple pattern
    5:l@n#f*m
    
    # Variable equation
    A=(4:*); B=(3:*); AB
    
    # Anagram search
    /landform
    ```
    """)

with col2:
    st.markdown("""
    **QAT Search Examples:**
    ```
    # Basic variable search
    A=(1-3:*);B=(1-3:*);A;B;AB
    
    # Multiple queries
    A=(2:*);B=(3:*);ABC - C=(1:*);D=(2:*);CD
    ```
    """)