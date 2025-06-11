import streamlit as st
import re
from itertools import product
import io

def matches_wildcard(seg, wild):
    vowels = set("aeiou")
    
    if wild == "*":
        return True
    if wild.endswith("*") and len(wild) == 2:
        return seg.startswith(wild[0])
    if len(wild) == len(seg):
        for c, w in zip(seg, wild):
            if w == "@" and c not in vowels:
                return False
            elif w == "#" and c in vowels:
                return False
            elif w not in "@#*" and w != c:
                return False
        return True
    if wild.startswith("[") and wild.endswith("]") and wild.count("[") == 1:
        negated = wild[1] == '!'
        char_set = set(wild[2:-1]) if negated else set(wild[1:-1])
        return all((c not in char_set) if negated else (c in char_set) for c in seg)
    if wild.endswith("*") and wild.startswith("[") and wild.count("[") == 1:
        part = re.match(r'(\[!?[a-z]+\])\*', wild)
        if part and len(seg) == 2:
            bracket = part.group(1)
            negated = bracket[1] == '!'
            chars = set(bracket[2:-1]) if negated else set(bracket[1:-1])
            return (seg[0] not in chars if negated else seg[0] in chars)
    if wild.count("[") > 1:
        parts = re.findall(r'\[.*?\]', wild)
        if len(parts) != len(seg):
            return False
        for c, part in zip(seg, parts):
            negated = part[1] == '!'
            char_set = set(part[2:-1]) if negated else set(part[1:-1])
            if (negated and c in char_set) or (not negated and c not in char_set):
                return False
        return True
    return False

def search_single_query(query, word_set):
    results = []
    
    var_ranges = {}
    prefix_map = {}
    extra_chars_per_var = {}
    wildcard_type = {}
    steps = []

    raw_parts = query.strip().split(';')
    for part in raw_parts:
        match_def_range = re.match(r'^([A-Z])=\((\d+)-(\d+):(.+)\)$', part.strip())
        match_def_fixed = re.match(r'^([A-Z])=\((\d+):(.+)\)$', part.strip())
        match_step = re.match(r'^[a-z.]*[A-Z]+[.]*$', part.strip())

        if match_def_range:
            var, min_len, max_len, pattern = match_def_range.groups()
            var_ranges[var] = (int(min_len), int(max_len))
            wildcard_type[var] = pattern.strip() if pattern.strip() else '*'
        elif match_def_fixed:
            var, length, pattern = match_def_fixed.groups()
            var_ranges[var] = (int(length), int(length))
            wildcard_type[var] = pattern.strip() if pattern.strip() else '*'
        elif match_step:
            steps.append(part.strip())

    if not steps:
        return ["[!] No valid steps found."]

    declared_vars = list(var_ranges.keys())

    combo_step = steps[-1]
    combo_match = re.match(r'^([a-z.]*)?([A-Z]+)(\.*)$', combo_step)
    if not combo_match:
        return ["[!] Invalid final combination step."]

    combo_prefix = combo_match.group(1) or ""
    combo_final_order = list(combo_match.group(2))
    combo_extra_chars = len(combo_match.group(3))

    for step in steps[:-1]:
        match = re.match(r'^([a-z]*)([A-Z])([.]*)$', step)
        if match:
            pre, var, dots = match.groups()
            prefix_map[var] = pre
            extra_chars_per_var[var] = len(dots or "")

    var_tail_map = {}
    for var in declared_vars:
        min_len, max_len = var_ranges[var]
        prefix = prefix_map.get(var, "")
        extra = extra_chars_per_var.get(var, 0)
        wild = wildcard_type.get(var, '*')
        match_dict = {}

        for word in word_set:
            if not word.startswith(prefix):
                continue
            tail = word[len(prefix):]
            for length in range(min_len, max_len + 1):
                if len(tail) == length + extra:
                    seg = tail[:length]
                    if matches_wildcard(seg, wild):
                        match_dict[seg] = word
        var_tail_map[var] = match_dict

    match_count = 0
    found = False

    var_segments = [list(var_tail_map[v].items()) for v in combo_final_order]
    for combo in product(*var_segments):
        tail_parts = [seg for seg, _ in combo]
        full_combo_core = combo_prefix + ''.join(tail_parts)
        if full_combo_core in word_set:
            tail_lookup = {v: seg for v, (seg, _) in zip(combo_final_order, combo)}
            final_words = []
            valid = True
            for var in declared_vars:
                seg = tail_lookup.get(var)
                if not seg or seg not in var_tail_map[var]:
                    valid = False
                    break
                full_candidate = prefix_map.get(var, "") + seg
                full_word = var_tail_map[var][seg]
                if not full_word.startswith(full_candidate):
                    valid = False
                    break
                final_words.append(full_word)
            if valid:
                results.append(" | ".join(final_words) + f" || {full_combo_core}")
                match_count += 1
                found = True

    if not found:
        results.append("[NO MATCHES]")
    
    return results

st.set_page_config(page_title="QAT Search", layout="wide")

st.title("QAT Search")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Input")
    uploaded_file = st.file_uploader("Upload wordlist file", type=['txt'])
    
    if uploaded_file is not None:
        content = uploaded_file.read().decode('utf-8')
        word_set = {line.strip() for line in content.split('\n') if line.strip()}
        st.success(f"✅ Loaded {len(word_set)} words")
        
        query = st.text_area("Enter your query(s):", height=150, placeholder="Single query: A=(1-3:*);B=(1-3:*);A;B;AB\nMultiple queries: A=(1-3:*);B=(1-3:*);A;B;AB - A=(2:*);B=(3:*);ABC")
        
        run_button = st.button("🚀 Run Query", type="primary", use_container_width=True)
    else:
        st.info("📁 Please upload a wordlist file to begin")
        run_button = False
        query = ""

with col2:
    st.subheader("Results")
    
    if uploaded_file is not None and run_button and query.strip():
        with st.spinner("🔄 Processing query..."):
            queries = [q.strip() for q in query.split(' - ') if q.strip()]
            
            output_text = ""
            for i, single_query in enumerate(queries):
                if i > 0:
                    output_text += "\n\n" + "="*70 + "\n\n"
                
                output_text += f"Query {i+1}: {single_query}\n" + "="*50 + "\n\n"
                results = search_single_query(single_query, word_set)
                output_text += "\n".join(results)
            
            st.text_area("Output:", value=output_text, height=500)
    
    elif uploaded_file is not None and run_button and not query.strip():
        st.warning("⚠️ Please enter a query")
    
    elif uploaded_file is not None:
        st.info("💡 Enter a query and click 'Run Query' to see results")