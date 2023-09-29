import streamlit as st

st.header('Screen Width Checker')
st.write('''<h3>The app container is <span id="root-width"></span> x 
<span id="root-height"></span> px.</h3>
''', unsafe_allow_html=True)

js = '''
<script>
    var container = window.parent.document.getElementById("root")

    var width = window.parent.document.getElementById("root-width")
    var height = window.parent.document.getElementById("root-height")

    function update_sizing(){
        width.textContent = container.getBoundingClientRect()['width']
        height.textContent = window.parent.innerHeight
    }
    update_sizing()

    window.parent.addEventListener('resize', function(event) {
        update_sizing()
    }, true);
    
</script>
'''

st.components.v1.html(js)