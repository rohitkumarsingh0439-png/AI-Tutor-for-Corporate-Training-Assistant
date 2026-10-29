"""Initial dashboard prototype using synthetic training data."""

import pandas as pd
import plotly.express as px
import streamlit as st

from config import APP_SUBTITLE, APP_TITLE, is_openai_configured

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🎓",
    layout="wide",
)

COURSES = [
    {
        "id": "COM101",
        "title": "Professional Communication",
        "category": "Communication",
        "level": "Beginner",
        "duration": "2 hours",
        "description": "Build clear, respectful and effective workplace communication skills.",
    },
    {
        "id": "TEAM101",
        "title": "Teamwork and Collaboration",
        "category": "Teamwork",
        "level": "Beginner",
        "duration": "90 minutes",
        "description": "Practice collaboration, feedback and constructive conflict resolution.",
    },
    {
        "id": "LEAD101",
        "title": "Leadership Fundamentals",
        "category": "Leadership",
        "level": "Intermediate",
        "duration": "3 hours",
        "description": "Explore delegation, coaching, accountability and team development.",
    },
    {
        "id": "CYB101",
        "title": "Cybersecurity Awareness",
        "category": "Cybersecurity",
        "level": "Beginner",
        "duration": "60 minutes",
        "description": "Recognize phishing, protect information and follow safe digital practices.",
    },
    {
        "id": "ETH101",
        "title": "Workplace Ethics",
        "category": "Ethics",
        "level": "Beginner",
        "duration": "75 minutes",
        "description": "Understand professional conduct, integrity and responsible decisions.",
    },
    {
        "id": "PROD101",
        "title": "Productivity and Time Management",
        "category": "Productivity",
        "level": "Beginner",
        "duration": "90 minutes",
        "description": "Prioritize tasks, manage interruptions and plan focused work.",
    },
]

SAMPLE_PROGRESS = pd.DataFrame(
    [
        {"Department": "Engineering", "Completion rate": 78},
        {"Department": "Human Resources", "Completion rate": 91},
        {"Department": "Sales", "Completion rate": 68},
        {"Department": "Operations", "Completion rate": 84},
        {"Department": "Finance", "Completion rate": 73},
    ]
)

st.markdown(
    """
    <style>
    .main-headline {
        display: block;
        font-size: clamp(1.25rem, 2.1vw, 1.8rem);
        font-weight: 700;
        line-height: 1.3;
        white-space: nowrap;
        max-width: 100%;
        margin: 0;
    }
    .headline-underline {
        display: block;
        width: 100%;
        height: 3px;
        background-color: #2563eb;
        margin-top: 6px;
        margin-bottom: 12px;
    }
    @media (max-width: 600px) {
        .main-headline {
            font-size: clamp(0.85rem, 3.5vw, 1.25rem);
            letter-spacing: -0.03em;
        }
    }
    </style>
    <div class="main-headline">&#127891; AI Tutor for Corporate Training Assistant</div>
    <div class="headline-underline"></div>
    """,
    unsafe_allow_html=True,
)
st.caption(APP_SUBTITLE)


with st.sidebar:
    st.header("Workspace")
    view = st.radio(
        "Choose a view",
        ["Overview", "Course Library", "Training Management", "About"],
    )
    st.divider()
    st.caption("Development build · Synthetic data")

if view == "Overview":
    st.subheader("Learning overview")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Available courses", len(COURSES))
    col2.metric("Sample learners", "120")
    col3.metric("Average completion", "78%")
    col4.metric("Average assessment score", "82%")

    st.subheader("Sample department completion")
    fig = px.bar(
        SAMPLE_PROGRESS,
        x="Department",
        y="Completion rate",
        range_y=[0, 100],
        labels={"Completion rate": "Completion (%)"},
        title="Illustrative training completion by department",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Featured learning")
    featured = st.columns(3)
    for column, course in zip(featured, COURSES[:3]):
        with column:
            st.markdown(f"**{course['title']}**")
            st.caption(f"{course['category']} · {course['duration']}")
            st.write(course["description"])

elif view == "Course Library":
    st.subheader("Course library")
    categories = ["All"] + sorted({course["category"] for course in COURSES})
    selected_category = st.selectbox("Filter by category", categories)

    filtered_courses = [
        course
        for course in COURSES
        if selected_category == "All"
        or course["category"] == selected_category
    ]

    for course in filtered_courses:
        with st.container(border=True):
            st.markdown(f"### {course['title']}")
            st.caption(
                f"Course ID: {course['id']} · {course['level']} · "
                f"{course['duration']}"
            )
            st.write(course["description"])
            st.write(f"**Category:** {course['category']}")
            st.button(
                "View course (coming soon)",
                key=f"course_{course['id']}",
                disabled=True,
            )

elif view == "Training Management":
    st.subheader("Training management")
    st.write(
        "This area will support course assignment, training schedules, "
        "learner groups and completion monitoring."
    )
    st.warning(
        "Assignments are not yet saved or sent. Persistent storage, "
        "authentication and permission enforcement have not been implemented."
    )

    departments = [
        "Engineering",
        "Human Resources",
        "Sales",
        "Operations",
        "Finance",
    ]
    selected_department = st.selectbox("Example target department", departments)
    selected_course = st.selectbox(
        "Example course",
        COURSES,
        format_func=lambda course: course["title"],
    )
    st.write(f"Selected department: **{selected_department}**")
    st.write(f"Selected course: **{selected_course['title']}**")
    st.button("Assign training (coming soon)", disabled=True)

elif view == "About":
    st.subheader("About this prototype")
    st.markdown(
        """
        The planned platform will include:

        - Employee learning paths and course content
        - AI-assisted workplace learning
        - Quizzes, assessments and progress tracking
        - Manager dashboards and learning analytics
        - Training assignment and administration
        - Role-based access controls
        - Persistent database storage
        - Privacy safeguards and automated tests
        """
    )

st.divider()
st.caption(
    "Prototype only. Do not enter real employee records or confidential "
    "company information until security and access controls are implemented."
)