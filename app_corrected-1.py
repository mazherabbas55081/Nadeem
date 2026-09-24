import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PNPI - Pak Navy Polytechnic Institute",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== VIP CSS ==========
st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#0f2027 0%,#203a43 50%,#2c5364 100%);}
.main-title{
    background: linear-gradient(90deg,#FFD700,#FFA500,#FF8C00);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    font-size:3.2em;font-weight:900;text-align:center;padding:15px;letter-spacing:3px;
}
.sub-title{color:#FFD700;text-align:center;font-size:1.3em;font-weight:600;margin-bottom:25px;letter-spacing:2px;}
.section-header{
    background: linear-gradient(90deg,#1e3c72,#2a5298);
    color:#FFD700;padding:15px 25px;border-radius:12px;font-size:1.7em;
    font-weight:700;border-left:8px solid #FFD700;margin:20px 0;
    box-shadow:0 4px 15px rgba(0,0,0,0.4);
}
.vip-card{
    background: linear-gradient(135deg,#1a1a2e,#16213e);
    border:2px solid #FFD700;border-radius:15px;padding:20px;margin:10px 0;
    box-shadow:0 8px 25px rgba(255,215,0,0.15);
}
.vip-card h3{color:#FFD700;}
.vip-card p{color:#E0E0E0;}
.student-card{
    background: linear-gradient(135deg,#232526,#414345);
    border-left:5px solid #00D9FF;border-radius:10px;padding:15px;
    margin:8px 0;color:white;box-shadow:0 4px 15px rgba(0,217,255,0.2);
}
.student-card b{color:#00D9FF;}
.info-box{
    background: linear-gradient(135deg,#0f2027,#2c5364);
    border:2px dashed #FFD700;border-radius:12px;padding:20px;margin:15px 0;
    text-align:center;color:#FFD700;font-weight:600;
}
.pass-status{background:linear-gradient(90deg,#00b09b,#96c93d);color:white;
    padding:15px;border-radius:10px;font-size:1.5em;font-weight:bold;text-align:center;}
.fail-status{background:linear-gradient(90deg,#cb2d3e,#ef473a);color:white;
    padding:15px;border-radius:10px;font-size:1.5em;font-weight:bold;text-align:center;}
.reexam-status{background:linear-gradient(90deg,#f7971e,#ffd200);color:#1a1a2e;
    padding:15px;border-radius:10px;font-size:1.5em;font-weight:bold;text-align:center;}
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0f2027,#203a43);
    border-right:3px solid #FFD700;
}
.stTabs [data-baseweb="tab-list"]{background:linear-gradient(90deg,#1e3c72,#2a5298);border-radius:10px;padding:5px;}
.stTabs [data-baseweb="tab"]{color:#FFD700;font-weight:600;}
[data-testid="stMetricValue"]{color:#FFD700;font-size:2em;font-weight:900;}
.footer{background:linear-gradient(90deg,#0f2027,#2c5364);color:#FFD700;
    text-align:center;padding:20px;border-radius:10px;border-top:3px solid #FFD700;
    margin-top:40px;font-weight:600;}
</style>
""", unsafe_allow_html=True)

# ========== DATA ==========
semesters_data = {
    "Semester 1": [
        "Engineering Mathematics-I","Applied Physics","Applied Chemistry",
        "Engineering Drawing","Workshop Practice","Basic Electronics",
        "Introduction to Computing","Communication Skills"
    ],
    "Semester 2": [
        "Engineering Mathematics-II","Electrical Circuits","Mechanics of Materials",
        "Digital Logic Design","Thermodynamics","Machine Drawing","Technical Writing"
    ],
    "Semester 3": [
        "Engineering Mathematics-III","Microprocessors","Sensors & Actuators",
        "Fluid Mechanics","Control Systems-I","CAD/CAM","Industrial Electronics"
    ],
    "Semester 4": [
        "Robotics & Automation","PLC Programming","Hydraulics & Pneumatics",
        "Control Systems-II","Embedded Systems"
    ],
    "Semester 5": [
        "Mechatronics System Design","Industrial IoT","AI in Automation",
        "Final Year Project","Industrial Training"
    ]
}

teachers_data = {
    "Engineering Mathematics-I":"Prof. Ahmed Raza","Applied Physics":"Dr. Sana Khan",
    "Applied Chemistry":"Prof. Bilal Ahmed","Engineering Drawing":"Engr. Usman Tariq",
    "Workshop Practice":"Mr. Kamran Ali","Basic Electronics":"Engr. Fatima Noor",
    "Introduction to Computing":"Prof. Hassan Raza","Communication Skills":"Ms. Ayesha Siddiqui",
    "Engineering Mathematics-II":"Prof. Ahmed Raza","Electrical Circuits":"Engr. Fatima Noor",
    "Mechanics of Materials":"Engr. Usman Tariq","Digital Logic Design":"Prof. Hassan Raza",
    "Thermodynamics":"Dr. Sana Khan","Machine Drawing":"Engr. Usman Tariq",
    "Technical Writing":"Ms. Ayesha Siddiqui","Engineering Mathematics-III":"Prof. Ahmed Raza",
    "Microprocessors":"Prof. Hassan Raza","Sensors & Actuators":"Engr. Fatima Noor",
    "Fluid Mechanics":"Dr. Sana Khan","Control Systems-I":"Engr. Zainab Malik",
    "CAD/CAM":"Engr. Usman Tariq","Industrial Electronics":"Engr. Fatima Noor",
    "Robotics & Automation":"Engr. Zainab Malik","PLC Programming":"Prof. Hassan Raza",
    "Hydraulics & Pneumatics":"Dr. Sana Khan","Control Systems-II":"Engr. Zainab Malik",
    "Embedded Systems":"Prof. Hassan Raza","Mechatronics System Design":"Engr. Zainab Malik",
    "Industrial IoT":"Prof. Hassan Raza","AI in Automation":"Dr. Sana Khan",
    "Final Year Project":"Engr. Zainab Malik","Industrial Training":"Mr. Kamran Ali"
}

students_data = {
    "PNPI-2024-001":{"name":"Muhammad Ali Khan","marks":{
        "Engineering Mathematics-I":85,"Applied Physics":78,"Applied Chemistry":72,
        "Engineering Drawing":88,"Workshop Practice":90,"Basic Electronics":75,
        "Introduction to Computing":82,"Communication Skills":80}},
    "PNPI-2024-002":{"name":"Hassan Ahmed","marks":{
        "Engineering Mathematics-I":55,"Applied Physics":58,"Applied Chemistry":62,
        "Engineering Drawing":70,"Workshop Practice":75,"Basic Electronics":65,
        "Introduction to Computing":60,"Communication Skills":68}},
    "PNPI-2024-003":{"name":"Fatima Zahra","marks":{
        "Engineering Mathematics-I":92,"Applied Physics":88,"Applied Chemistry":85,
        "Engineering Drawing":90,"Workshop Practice":95,"Basic Electronics":89,
        "Introduction to Computing":91,"Communication Skills":87}},
    "PNPI-2024-004":{"name":"Ayesha Siddiqui","marks":{
        "Engineering Mathematics-I":48,"Applied Physics":52,"Applied Chemistry":45,
        "Engineering Drawing":60,"Workshop Practice":65,"Basic Electronics":55,
        "Introduction to Computing":58,"Communication Skills":62}},
    "PNPI-2024-005":{"name":"Bilal Hussain","marks":{
        "Engineering Mathematics-I":75,"Applied Physics":80,"Applied Chemistry":78,
        "Engineering Drawing":82,"Workshop Practice":85,"Basic Electronics":79,
        "Introduction to Computing":77,"Communication Skills":81}},
    "PNPI-2024-006":{"name":"Zainab Malik","marks":{
        "Engineering Mathematics-I":88,"Applied Physics":85,"Applied Chemistry":90,
        "Engineering Drawing":87,"Workshop Practice":92,"Basic Electronics":86,
        "Introduction to Computing":89,"Communication Skills":84}},
    "PNPI-2024-007":{"name":"Usman Tariq","marks":{
        "Engineering Mathematics-I":65,"Applied Physics":68,"Applied Chemistry":70,
        "Engineering Drawing":72,"Workshop Practice":75,"Basic Electronics":66,
        "Introduction to Computing":69,"Communication Skills":71}},
    "PNPI-2024-008":{"name":"Kamran Ali","marks":{
        "Engineering Mathematics-I":58,"Applied Physics":55,"Applied Chemistry":60,
        "Engineering Drawing":65,"Workshop Practice":68,"Basic Electronics":62,
        "Introduction to Computing":64,"Communication Skills":66}},
}

# ========== HEADER ==========
st.markdown("""
<div style="text-align:center;">
<img src="assets/logo.png" width="180">
<div class="main-title">🎓 PAK NAVY POLYTECHNIC INSTITUTE</div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="sub-title">⚓ PNPI | West Wharf Road, Karachi ⚓</div>', unsafe_allow_html=True)

# ========== SIDEBAR ==========
st.sidebar.markdown("## 🧭 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Select Page:", [
    "🏠 Home","🎓 Technology","📚 Study Course",
    "🔬 Labs & Facilities","📊 Student Results","🎯 About Us"
])
st.sidebar.markdown("---")
st.sidebar.info("📍 **West Wharf Road, Karachi**\n\nPak Navy Polytechnic Institute")
st.sidebar.success("✅ Est. under Pakistan Navy")

# ========== HOME ==========
if page == "🏠 Home":
    col1,col2 = st.columns([1,2])
    with col1:
        st.image("assets/campus.jpg",
                 caption="PNPI Main Campus", use_container_width=True)
    with col2:
        st.markdown("""<div class="info-box">
        <h2>🏛️ Welcome to PNPI</h2>
        <p>Pakistan Navy Polytechnic Institute is a premier technical institution at 
        West Wharf Road, Karachi. Committed to excellence in technical education.</p>
        </div>""", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🏫 Our Campus</div>', unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    c1.image("assets/campus.jpg", caption="Main Building", use_container_width=True)
    c2.image("assets/classroom.jpg", caption="Classrooms", use_container_width=True)
    c3.image("assets/campus.jpg", caption="Campus View", use_container_width=True)
    st.markdown('<div class="section-header">📊 Quick Stats</div>', unsafe_allow_html=True)
    m1,m2,m3,m4 = st.columns(4)
    m1.metric("🎓 Technology","1","Mechatronic")
    m2.metric("📚 Semesters","5","Total")
    m3.metric("👨‍🎓 Students","8","Per Semester")
    m4.metric("🏫 Classrooms","20","Available")

# ========== TECHNOLOGY ==========
elif page == "🎓 Technology":
    st.markdown('<div class="section-header">⚙️ Mechatronic Engineering</div>', unsafe_allow_html=True)
    st.image("assets/lab.jpg",
             caption="Mechatronic Engineering Lab", use_container_width=True)
    st.markdown("""<div class="vip-card">
    <h3>🤖 About Mechatronic Engineering</h3>
    <p>Combines Mechanical, Electronics, Computer Science, and Control Systems 
    for modern industrial automation and robotics.</p></div>""", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📖 5 Semester Breakdown</div>', unsafe_allow_html=True)
    for sem,subs in semesters_data.items():
        with st.expander(f"📘 {sem} — {len(subs)} Subjects"):
            st.markdown(f"**Subjects:** {len(subs)} | **Students:** 8")
            for i,s in enumerate(subs,1):
                st.markdown(f"""<div class="student-card">
                <b>{i}. {s}</b><br>👨‍🏫 {teachers_data.get(s,'TBA')}</div>""",
                unsafe_allow_html=True)

# ========== STUDY COURSE ==========
elif page == "📚 Study Course":
    st.markdown('<div class="section-header">📚 Study Course & Teachers</div>', unsafe_allow_html=True)
    st.image("assets/classroom.jpg",
             caption="Study Environment", use_container_width=True)
    for sem,subs in semesters_data.items():
        st.markdown(f"### 🎯 {sem}")
        df = pd.DataFrame({"Subject":subs,"Teacher":[teachers_data.get(s,"TBA") for s in subs]})
        df.index = df.index + 1
        st.dataframe(df, use_container_width=True)
        st.markdown("---")

# ========== LABS ==========
elif page == "🔬 Labs & Facilities":
    st.markdown('<div class="section-header">🔬 Mechatronic Lab</div>', unsafe_allow_html=True)
    st.image("assets/lab.jpg",
             caption="Mechatronic Lab", use_container_width=True)
    st.markdown('<div class="section-header">📚 Library</div>', unsafe_allow_html=True)
    st.image("assets/library.jpg",
             caption="Central Library", use_container_width=True)
    st.markdown('<div class="section-header">🏏 Cricket Group</div>', unsafe_allow_html=True)
    st.image("assets/cricket.jpg",
             caption="PNPI Cricket Team", use_container_width=True)
    st.markdown('<div class="section-header">🍽️ Canteen</div>', unsafe_allow_html=True)
    st.image("assets/canteen.jpg",
             caption="College Canteen", use_container_width=True)
    st.markdown('<div class="section-header">🏫 20 Classrooms</div>', unsafe_allow_html=True)
    st.image("assets/classroom.jpg",
             caption="Modern Classrooms", use_container_width=True)
    cols = st.columns(4)
    for i in range(20):
        with cols[i % 4]:
            st.markdown(f"""<div class="student-card">
            <b>🏫 Classroom {i+1}</b><br>Capacity: 40 Students</div>""",
            unsafe_allow_html=True)

# ========== RESULTS ==========
elif page == "📊 Student Results":
    st.markdown('<div class="section-header">🔐 Student Login Portal</div>', unsafe_allow_html=True)
    st.image("assets/classroom.jpg",
             caption="Result Portal", use_container_width=True)
    st.markdown("""<div class="info-box">
    <h3>📝 Enter Credentials to View Results</h3>
    <p>Use your registered Name and Roll Number</p></div>""", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        name = st.text_input("👤 Student Name", placeholder="e.g. Muhammad Ali Khan")
    with c2:
        roll = st.text_input("🔢 Roll Number", placeholder="e.g. PNPI-2024-001")
    if st.button("🔍 Show My Result", use_container_width=True):
        if roll in students_data:
            if students_data[roll]["name"].lower() == name.lower().strip():
                s = students_data[roll]
                marks = s["marks"]
                st.success(f"✅ Welcome, {s['name']}!")
                st.markdown(f"### 📋 Roll Number: `{roll}`")
                st.markdown("---")
                df = pd.DataFrame({
                    "Subject":list(marks.keys()),
                    "Marks":list(marks.values()),
                    "Percentage":[f"{v}%" for v in marks.values()],
                    "Status":["✅ Pass" if v>=60 else "❌ Fail" for v in marks.values()]
                })
                df.index = df.index + 1
                st.dataframe(df, use_container_width=True)
                failed = sum(1 for v in marks.values() if v<60)
                total = sum(marks.values())
                avg = total/len(marks)
                st.markdown("---")
                a,b,c = st.columns(3)
                a.metric("📊 Total Marks", f"{total}/{len(marks)*100}")
                b.metric("📈 Average", f"{avg:.2f}%")
                c.metric("❌ Failed Subjects", failed)
                st.markdown("---")
                st.markdown("### 🎯 Final Status")
                if failed == 0:
                    st.markdown('<div class="pass-status">🎉 PASSED — All subjects cleared!</div>', unsafe_allow_html=True)
                elif failed in [1,2]:
                    st.markdown(f'<div class="reexam-status">⚠️ RE-EXAM REQUIRED — {failed} subject(s)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="fail-status">❌ FAILED — {failed} subjects below 60%</div>', unsafe_allow_html=True)
            else:
                st.error("❌ Name does not match with Roll Number!")
        else:
            st.error("❌ Invalid Roll Number!")
        with st.expander("📋 Demo Credentials"):
            for r,d in students_data.items():
                st.write(f"**{r}** → {d['name']}")

# ========== ABOUT ==========
elif page == "🎯 About Us":
    st.markdown('<div class="section-header">🎯 About PNPI</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200",
             caption="PNPI Campus", use_container_width=True)
    st.markdown("""<div class="vip-card">
    <h3>🏛️ Pak Navy Polytechnic Institute</h3>
    <p><b>Location:</b> West Wharf Road, Karachi, Pakistan</p>
    <p><b>Affiliation:</b> Pakistan Navy</p>
    <p><b>Technology:</b> Mechatronic Engineering (5 Semesters)</p>
    <p><b>Facilities:</b> 20 Classrooms, Labs, Library, Cricket Ground, Canteen</p>
    </div>""", unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("""<div class="footer">
⚓ Pak Navy Polytechnic Institute (PNPI) | West Wharf Road, Karachi ⚓<br>
© 2026 All Rights Reserved | Made with ❤️ using Python & Streamlit
</div>""", unsafe_allow_html=True)
