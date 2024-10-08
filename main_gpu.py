from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

data = [
    {
        "PERSON_NAME": [
            "Nguyen Minh Quan"
        ],
        "JOB_TITLE": [
            "Researcher",
            "Junior Data Scientist"
        ],
        "ORGANIZATION": [
            "HUTECH",
            "University of Natural Science VNUHCM who",
            "University of Technology HUTECH",
            "Tiki Shop"
        ],
        "EDUCATION": [
            "B.E"
        ],
        "MAJOR": [
            "Information Technology",
            "Natural Language Processing"
        ],
        "GPA": [
            "GPA 3.33",
            "GPA 3.8"
        ],
        "SKILL": [
            "AutoML",
            "Heroku",
            "graph theory",
            "Testing",
            "PySpark",
            "BIG DATA",
            "Scrapy A/B",
            "JavaScript",
            "Java",
            "Artificial Intelligence",
            "CMT",
            "Teamworks",
            "R",
            "Powershell",
            "Swimming",
            "Discrete math",
            "Research Presentations",
            "C",
            "Vim",
            "Deep Learning",
            "Scrapping data",
            "visualization",
            "pipeline",
            "Data science",
            "Data structures",
            "Research new technology",
            "Data Visualization and Analysis",
            "Reporting",
            "Communicating",
            "filtering",
            "Time Series",
            "Database Management",
            "Python",
            "Github",
            "HTML",
            "AI",
            "Git",
            "Machine Learning",
            "Analysis",
            "SQL",
            "MARCHINE",
            "clustering algorithms",
            "data analysis",
            "Data Science",
            "NLP",
            "Linear algebra",
            "chatbot",
            "OCR",
            "CSS",
            "Programing",
            "Big Data",
            "Object oriented",
            "Self learning",
            "Writing",
            "Problem solving",
            "Regression",
            "Mathematics",
            "Applied",
            "Calculus",
            "RFM",
            "Statistics",
            "Team leader"
        ],
        "EMAIL": [
            "minhquan23102000@gmail.com"
        ],
        "PROFILE_URL": [
            "github.com"
        ],
        "PHONE": [
            "0383666401"
        ]
    },
    {
        "ORGANIZATION": [
            "VINAI VINGROUP",
            "TOP 7",
            "Front End App",
            "FPT AI CTA Consolation",
            "TOP 24 Makethon",
            "Ba Dam Market Thoi Lai Can Tho City Poem",
            "Scholoship KMS Technology CityNow",
            "Vietnam National University Ho Chi Minh",
            "RUN FOR ORPHANS",
            "HCM CITY UNIVERSITY OF TECHNOLOGY HUTECH"
        ],
        "MAJOR": [
            "Information Technology",
            "Software Technology",
            "Computer Vision"
        ],
        "GPA": [
            "GPA 3.76/4.00",
            "3.97/4.00"
        ],
        "PERSON_NAME": [
            "NGUYEN TRONG NHAN HUTECH",
            "XUAN THOI LAI",
            "MR PHAM"
        ],
        "SKILL": [
            "Statistical Probability",
            "Math",
            "language processor",
            "Run for childrenorphan",
            "Linear",
            "AI Challenge",
            "Scholoship",
            "Collaborator",
            "API building",
            "Identify and extract personal information",
            "Calculus",
            "frameworkTensorflow",
            "Compilation",
            "Computer Vision",
            "BLOG",
            "image analysis",
            "Yolo",
            "Fresher",
            "Logistic vision",
            "Regression",
            "BOT",
            "Linear Algebra",
            "Communication",
            "image processing"
        ],
        "GENDER": [
            "Male"
        ],
        "JOB_TITLE": [
            "professional engineer"
        ],
        "EMAIL": [
            "nguyennhan8521@gmail.com"
        ],
        "PROFILE_URL": [
            "github.com/NTNhacker/DOAN_JAVA",
            "www.youtube.com/watch",
            "fb.com/nhan.n.trong.33",
            "topcv.vn"
        ],
        "PHONE": [
            "0866039411"
        ]
    }
]

from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)




def generate_output(inputs):

    conversation = [
        {
            "role": "system",
            "content": f"You are a helpful assistant. Use below information to answer the question from user. \n Information: {str(data)}"
        },
        {
            "role": "user",
            "content": "hi"
        },
        {
            "role": "assistant",
            "content": "how i can help you?"
        },
        {
            "role": "user",
            "content": "How many resumes are there?"
        },
        {
            "role": "assistant",
            "content": """Based on the given information, there are 2 resumes provided. The resumes belong to Nguyen Minh Quan and Nguyen Trong Nhan HUTECH. Each person's resume is presented as a dictionary with various key-value pairs, such as PERSON_NAME, JOB_TITLE, ORGANIZATION, EDUCATION, MAJOR, SKILL, GPA, EMAIL, PROFILE_URL, GENDER, JOB_TITLE, and PHONE. So, in total, there are 2 resumes with different sets of information."""
        },
        {
            "role": "user",
            "content": "Give me some information about second resume"
        },
        {
            "role": "user",
            "content": """Sure! Here's some information about the second resume:

- Person's Name: Nguyen Trong Nhan HUTECH
- Job Title: Not explicitly mentioned in the given information
- Organizations: Listed as "VINAI VINGROUP", "TOP 7", "Front End App", "FPT AI CTA Consolation", "TOP 24 Makethon", "Ba Dam Market Thoi Lai Can Tho City Poem", "Scholoship KMS Technology CityNow", "Vietnam National University Ho Chi Minh", "RUN FOR ORPHANS", and "HCM CITY UNIVERSITY OF TECHNOLOGY HUTECH". It's not clear if he has worked in all of these organizations or if he has held different job titles in some of them.
- Education: Holds a degree with a GPA of 3.76/4.00 from Vietnam National University Ho Chi Minh.
- Major: Listed as "Information Technology" and "Software Technology" for two different organizations.
- Skills: Includes "Statistical Probability", "Math", "language processor", "Run for childrenorphan", "Linear", "AI Challenge", "Scholoship", "Collaborator", "API building", "Identify and extract personal information", "Calculus", "frameworkTensorflow", "Compilation", "Computer Vision", "BLOG", "image analysis", "Yolo", "Fresher", "Logistic vision", "Regression", "BOT", "Linear Algebra", "Communication", and "image processing".
- Email: nguyennhan8521@gmail.com
- Profile URL: Listed as "github.com/NTNhacker/DOAN_JAVA", "www.youtube.com/watch", and "fb.com/nhan.n.trong.33". It's not clear which profile URL corresponds to which organization.
- Phone number: 0866039411
- Gender: Mentioned as "Male"."""
        },
        {
            "role": "user",
            "content": inputs
        },
    ]
    completion = client.chat.completions.create(
        model="HuggingFaceH4/zephyr-7b-beta",
        messages=conversation,
        stream = True
    )
    # raw_ans = ""

    for i in completion:
        curr = i.choices[0].delta.content
        if curr:
            yield str(curr)
    return ""


@app.post("/")
def main(inputs: str = ""):
    print(inputs)
    return StreamingResponse(generate_output(inputs))