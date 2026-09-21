import streamlit as st
from pathlib import Path

# ============================================================
# AERIS WEBSITE
# ============================================================

st.set_page_config(
    page_title="AERIS | Drink Smart. Live Better.",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent

# Images are stored in the SAME folder as app.py
ASSETS = BASE_DIR


# ============================================================
# HELPERS
# ============================================================

def image_path(filename):
    """
    Returns the full path to an image stored
    in the same folder as app.py.
    """
    return str(ASSETS / filename)


def html(content):
    st.html(content)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "cart" not in st.session_state:
    st.session_state.cart = 0


# ============================================================
# GLOBAL CSS
# ============================================================

html("""
<style>

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    background: #031015;
}

[data-testid="stAppViewContainer"] {
    background: #031015 !important;
}

[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    padding: 0 !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =========================================================
   NAVBAR
   ========================================================= */

.navbar {
    height: 70px;

    display: flex;
    align-items: center;

    padding: 0 7%;

    background: #031015;

    border-bottom:
        1px solid
        rgba(255,255,255,.10);
}

.logo-symbol {
    color: white;
    font-size: 29px;
    margin-right: 11px;
}

.logo {
    color: white;
    font-size: 21px;
    letter-spacing: 8px;
    font-weight: 400;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    min-height: 650px;

    display: flex;
    align-items: center;

    padding: 70px 8%;

    background-image:
        linear-gradient(
            90deg,
            rgba(2,16,22,.94) 0%,
            rgba(2,16,22,.62) 40%,
            rgba(2,16,22,.08) 80%
        ),
        url("__HERO_IMAGE__");

    background-size: cover;
    background-position: center;
}

.hero-content {
    max-width: 590px;
}

.eyebrow {
    color: #a7ffdf;

    font-size: 11px;

    letter-spacing: 3px;

    text-transform: uppercase;

    margin-bottom: 18px;
}

.hero-title {
    color: white;

    font-size:
        clamp(52px, 6vw, 85px);

    font-weight: 400;

    line-height: .97;

    margin: 0 0 25px;
}

.hero-text {
    color:
        rgba(255,255,255,.86);

    font-size: 18px;

    line-height: 1.55;

    max-width: 470px;
}

.hero-button {
    display: inline-block;

    margin-top: 24px;

    padding: 12px 25px;

    border:
        1px solid
        white;

    border-radius: 999px;

    color: white;

    font-size: 14px;
}

.hero-features {
    display: flex;

    gap: 25px;

    flex-wrap: wrap;

    margin-top: 32px;

    color: #d8e4e1;

    font-size: 13px;
}


/* =========================================================
   SECTIONS
   ========================================================= */

.section {
    padding: 75px 8%;

    background: #031015;
}

.light-section {
    padding: 75px 8%;

    background: #f2f0ea;

    color: #071216;
}

.title {
    color: white;

    font-size:
        clamp(36px, 4.5vw, 55px);

    font-weight: 400;

    line-height: 1.05;

    margin-bottom: 18px;
}

.light-section .title {
    color: #071216;
}

.text {
    color: #aebfbc;

    max-width: 620px;

    font-size: 16px;

    line-height: 1.7;
}

.light-section .text {
    color: #4d595b;
}


/* =========================================================
   CARDS
   ========================================================= */

.card {
    min-height: 190px;

    padding: 28px;

    border-radius: 20px;

    border:
        1px solid
        rgba(165,255,220,.16);

    background:
        linear-gradient(
            145deg,
            #0a2527,
            #061418
        );
}

.icon {
    color: #a7ffdf;

    font-size: 30px;
}

.card-title {
    color: white;

    font-size: 20px;

    margin-top: 15px;

    margin-bottom: 10px;
}

.card-text {
    color: #aebfbc;

    font-size: 14px;

    line-height: 1.6;
}


/* =========================================================
   SEGMENTATION
   ========================================================= */

.segment {
    min-height: 145px;

    padding: 24px;

    margin-bottom: 15px;

    border-radius: 15px;

    background: #071e24;

    border:
        1px solid
        rgba(255,255,255,.08);
}

.segment-title {
    color: white;

    font-size: 18px;

    margin-bottom: 10px;
}

.segment-text {
    color: #aebfbc;

    font-size: 13px;

    line-height: 1.6;
}


/* =========================================================
   FUNNEL
   ========================================================= */

.funnel {
    display: flex;

    gap: 8px;

    flex-wrap: wrap;
}

.funnel-item {
    flex: 1;

    min-width: 160px;

    text-align: center;

    padding: 25px 10px;

    border-top:
        1px solid
        rgba(165,255,220,.30);
}

.funnel-number {
    width: 50px;
    height: 50px;

    margin: 0 auto 15px;

    display: flex;

    align-items: center;
    justify-content: center;

    border:
        1px solid
        #a7ffdf;

    border-radius: 50%;

    color: #a7ffdf;
}

.funnel-title {
    color: white;

    font-size: 13px;

    font-weight: 600;
}

.funnel-text {
    color: #8fa39f;

    font-size: 12px;

    margin-top: 8px;
}


/* =========================================================
   SHOP
   ========================================================= */

.shop-box {
    padding: 35px;

    border-radius: 24px;

    border:
        1px solid
        rgba(165,255,220,.16);

    background:
        linear-gradient(
            135deg,
            #0a2025,
            #031014
        );
}

.price {
    color: white;

    font-size: 38px;

    margin: 20px 0;
}


/* =========================================================
   STREAMLIT BUTTONS
   ========================================================= */

div.stButton > button {
    min-height: 42px !important;

    padding:
        8px 18px !important;

    border-radius:
        999px !important;

    background:
        rgba(3,16,21,.55) !important;

    border:
        1px solid
        rgba(167,255,223,.48) !important;

    color:
        #f7fbfa !important;

    font-size:
        13px !important;

    font-weight:
        500 !important;

    box-shadow:
        none !important;

    transition:
        .2s ease !important;
}

div.stButton > button:hover {
    background:
        rgba(167,255,223,.10) !important;

    border-color:
        #a7ffdf !important;

    transform:
        translateY(-1px);
}


/* =========================================================
   IMAGES
   ========================================================= */

[data-testid="stImage"] {
    margin-top: 5px !important;

    margin-bottom: 10px !important;
}

[data-testid="stImage"] img {
    width: 100% !important;

    display: block !important;

    border-radius: 18px !important;
}


/* =========================================================
   INPUTS
   ========================================================= */

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input {
    background: #08191e !important;

    color: white !important;

    border:
        1px solid
        rgba(167,255,223,.18) !important;

    border-radius: 10px !important;
}

[data-testid="stSelectbox"] > div > div {
    background: #08191e !important;

    border:
        1px solid
        rgba(167,255,223,.18) !important;

    border-radius: 10px !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    padding: 38px 8%;

    border-top:
        1px solid
        rgba(255,255,255,.08);

    background: #031015;

    color: #7f918d;

    font-size: 12px;
}

.footer-logo {
    color: white;

    letter-spacing: 6px;
}


/* =========================================================
   MOBILE
   ========================================================= */

@media(max-width:800px) {

    .hero {
        min-height: 600px;

        padding: 55px 6%;

        background-position:
            65% center;
    }

    .hero-title {
        font-size: 50px;
    }

    .section,
    .light-section {
        padding: 55px 6%;
    }

    .funnel {
        flex-direction: column;
    }

    .funnel-item {
        min-width: 100%;
    }

}

</style>
""")


# ============================================================
# HERO IMAGE
# ============================================================

hero_image_path = image_path("1.jpeg")

hero_image = ""

try:
    hero_bytes = Path(hero_image_path).read_bytes()

    import base64

    hero_encoded = base64.b64encode(
        hero_bytes
    ).decode("utf-8")

    hero_image = (
        f"data:image/jpeg;base64,{hero_encoded}"
    )

except Exception:
    hero_image = ""


# Replace placeholder in the CSS with actual image
html(f"""
<style>

.hero {{
    background-image:
        linear-gradient(
            90deg,
            rgba(2,16,22,.94) 0%,
            rgba(2,16,22,.62) 40%,
            rgba(2,16,22,.08) 80%
        ),
        url("{hero_image}");
}}

</style>
""")


# ============================================================
# NAVBAR
# ============================================================

html("""
<div class="navbar">

    <span class="logo-symbol">
        ♢
    </span>

    <span class="logo">
        AERIS
    </span>

</div>
""")


# ============================================================
# NAVIGATION
# ============================================================

nav = st.columns(
    [4.4, 1, 1, 1, 1, 1, .6]
)

pages = [
    ("Home", nav[1]),
    ("Shop", nav[2]),
    ("Features", nav[3]),
    ("About", nav[4]),
    ("Contact", nav[5]),
]

for name, column in pages:

    with column:

        if st.button(
            name,
            key=f"nav_{name}",
            use_container_width=True
        ):

            st.session_state.page = name

            st.rerun()


with nav[6]:

    html(f"""
    <div style="
        text-align:center;
        color:#a7ffdf;
        padding-top:10px;
        font-size:14px;
    ">
        🛒 {st.session_state.cart}
    </div>
    """)


# ============================================================
# HOME
# ============================================================

def home():

    # ========================================================
    # HERO
    # ========================================================

    html("""
    <div class="hero">

        <div class="hero-content">

            <div class="eyebrow">
                SMART HYDRATION • MODERN LIFESTYLE
            </div>

            <div class="hero-title">
                Drink Smart.<br>
                Live Better.
            </div>

            <div class="hero-text">
                A smart, reusable hydration companion
                for modern lifestyles.
            </div>

            <div class="hero-button">
                Shop Now&nbsp;&nbsp; →
            </div>

            <div class="hero-features">

                <span>
                    ♧ Smart
                </span>

                <span>
                    ⌁ Stylish
                </span>

                <span>
                    ◉ Sustainable
                </span>

            </div>

        </div>

    </div>
    """)


    # ========================================================
    # PRODUCT
    # ========================================================

    html("""
    <div class="section">

        <div class="eyebrow">
            01 — THE PRODUCT
        </div>

    </div>
    """)


    left, right = st.columns(
        [1, 1.35],
        gap="large"
    )


    # ========================================================
    # PRODUCT INFORMATION
    # ========================================================

    with left:

        html("""
        <div>

            <div class="eyebrow">
                AERIS ONE
            </div>

            <div class="title">
                More than a bottle.
            </div>

            <div class="text">

                A smart hydration companion
                designed for modern routines.

                AERIS One combines intelligent
                hydration reminders, live temperature
                indication and an insulated body
                into one sleek everyday bottle.

            </div>


            <div style="
                display:flex;
                gap:35px;
                flex-wrap:wrap;
                margin-top:30px;
                margin-bottom:25px;
            ">


                <div>

                    <div style="
                        color:#a7ffdf;
                        font-size:24px;
                        font-weight:500;
                    ">
                        25°C
                    </div>

                    <div style="
                        color:#8fa39f;
                        font-size:11px;
                        letter-spacing:1px;
                        margin-top:5px;
                    ">
                        LIVE TEMPERATURE
                    </div>

                </div>


                <div>

                    <div style="
                        color:#a7ffdf;
                        font-size:24px;
                        font-weight:500;
                    ">
                        SMART
                    </div>

                    <div style="
                        color:#8fa39f;
                        font-size:11px;
                        letter-spacing:1px;
                        margin-top:5px;
                    ">
                        HYDRATION CUES
                    </div>

                </div>


                <div>

                    <div style="
                        color:#a7ffdf;
                        font-size:24px;
                        font-weight:500;
                    ">
                        INSULATED
                    </div>

                    <div style="
                        color:#8fa39f;
                        font-size:11px;
                        letter-spacing:1px;
                        margin-top:5px;
                    ">
                        TEMPERATURE RETENTION
                    </div>

                </div>


            </div>


            <div style="
                color:white;
                font-size:30px;
                font-weight:400;
                margin-bottom:20px;
            ">
                ₹2,499
            </div>


            <div class="text" style="
                font-size:13px;
                margin-bottom:25px;
            ">

                Built for college, office, gym and travel.
                Reusable, leak-resistant and designed
                to fit seamlessly into your everyday life.

            </div>

        </div>
        """)


        if st.button(
            "Explore Features →",
            key="explore",
            use_container_width=True
        ):

            st.session_state.page = "Features"

            st.rerun()


    # ========================================================
    # PRODUCT IMAGE
    # ========================================================

    with right:

        st.image(
            image_path("3.jpeg"),
            use_container_width=True
        )


    # ========================================================
    # FEATURES
    # ========================================================

    html("""
    <div class="section">

        <div class="eyebrow">
            SMART BY DESIGN
        </div>

        <div class="title">
            Built around your day.
        </div>

    </div>
    """)


    feature_data = [

        (
            "◌",
            "Smart Reminders",
            "LED indicator encourages regular hydration."
        ),

        (
            "◉",
            "Insulated",
            "Temperature-retaining, leak-proof design."
        ),

        (
            "♧",
            "Sustainable",
            "Reusable alternative to disposable bottles."
        ),

        (
            "⌂",
            "Lifestyle Design",
            "Made for college, office, gym and travel."
        ),

    ]


    feature_cols = st.columns(
        4,
        gap="medium"
    )


    for col, data in zip(
        feature_cols,
        feature_data
    ):

        icon, title, description = data

        with col:

            html(f"""
            <div class="card">

                <div class="icon">
                    {icon}
                </div>

                <div class="card-title">
                    {title}
                </div>

                <div class="card-text">
                    {description}
                </div>

            </div>
            """)


    # ========================================================
    # SEGMENTATION
    # ========================================================

    html("""
    <div class="light-section">

        <div class="eyebrow">
            02 — MARKET SEGMENTATION
        </div>

        <div class="title">
            Who are we targeting?
        </div>

        <div class="text">
            Four layers of segmentation create a focused audience.
        </div>

    </div>
    """)


    segments = [

        (
            "Demographic",
            "18–30 years • Students + young professionals • Moderate–high buying power"
        ),

        (
            "Geographic",
            "Mumbai • Navi Mumbai • Pune • Bengaluru • Delhi NCR • Hyderabad • Chennai"
        ),

        (
            "Psychographic",
            "Health & wellness • Digital-first • Eco-conscious • Design driven"
        ),

        (
            "Behavioural",
            "Online shoppers • Fitness viewers • Lifestyle-product buyers"
        ),

    ]


    left, right = st.columns(
        2,
        gap="medium"
    )


    for i, data in enumerate(segments):

        title, description = data

        target = left if i % 2 == 0 else right

        with target:

            html(f"""
            <div class="segment">

                <div class="segment-title">
                    {title}
                </div>

                <div class="segment-text">
                    {description}
                </div>

            </div>
            """)


    # ========================================================
    # FUNNEL
    # ========================================================

    html("""
    <div class="section">

        <div class="eyebrow">
            03 — CAMPAIGN FUNNEL
        </div>

        <div class="title">
            From awareness to advocacy
        </div>

        <div class="text">
            Every stage has a clear objective,
            content format and CTA.
        </div>

    </div>
    """)


    funnel = [

        (
            "01",
            "AWARENESS",
            "Reels • Shorts • Influencers"
        ),

        (
            "02",
            "INTEREST",
            "Carousels • Stories • Tips"
        ),

        (
            "03",
            "CONSIDERATION",
            "Reviews • Demos • FAQs"
        ),

        (
            "04",
            "CONVERSION",
            "Search • Retargeting • Offer"
        ),

        (
            "05",
            "RETENTION",
            "UGC • Reviews • Referrals"
        ),

    ]


    html('<div class="funnel">')

    for number, title, description in funnel:

        html(f"""
        <div class="funnel-item">

            <div class="funnel-number">
                {number}
            </div>

            <div class="funnel-title">
                {title}
            </div>

            <div class="funnel-text">
                {description}
            </div>

        </div>
        """)

    html("</div>")


    st.write("")


    # ========================================================
    # IMAGE STRIP
    # ========================================================

    image1, image2 = st.columns(
        2,
        gap="medium"
    )


    with image1:

        st.image(
            image_path("2.jpeg"),
            use_container_width=True
        )


    with image2:

        st.image(
            image_path("6.jpeg"),
            use_container_width=True
        )


# ============================================================
# SHOP
# ============================================================

def shop():

    html("""
    <div class="section">

        <div class="eyebrow">
            AERIS SMART BOTTLE
        </div>

        <div class="title">
            Meet AERIS One.
        </div>

    </div>
    """)


    image_col, product_col = st.columns(
        [1.2, 1],
        gap="large"
    )


    with image_col:

        st.image(
            image_path("3.jpeg"),
            use_container_width=True
        )


    with product_col:

        html("""
        <div class="shop-box">

            <div class="eyebrow">
                AERIS ONE
            </div>

            <div class="title">
                Smart hydration.
            </div>

            <div class="text">

                A premium smart hydration companion
                with temperature indication,
                reminder lighting and an insulated
                leak-proof design.

            </div>

            <div class="price">
                ₹2,499
            </div>

        </div>
        """)


        color = st.selectbox(
            "Choose your finish",
            [
                "Obsidian Black",
                "Lavender",
                "Sage Green"
            ]
        )


        quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=10,
            value=1
        )


        if st.button(
            "Add to Cart",
            key="cart_button",
            use_container_width=True
        ):

            st.session_state.cart += int(quantity)

            st.success(
                f"Added {quantity} × AERIS One "
                f"({color}) to your cart."
            )


        st.caption(
            f"Cart: {st.session_state.cart} item(s)"
        )


    html("""
    <div class="section">

        <div class="title">
            Your Everyday Companion
        </div>

    </div>
    """)


    image_col, text_col = st.columns(
        2,
        gap="large"
    )


    with image_col:

        st.image(
            image_path("2.jpeg"),
            use_container_width=True
        )


    with text_col:

        html("""
        <div class="card">

            <div class="eyebrow">
                DESIGNED FOR REAL LIFE
            </div>

            <div class="card-title">
                College · Office · Gym · Travel
            </div>

            <div class="card-text">

                AERIS is built to move with you,
                from your first class to your last workout.

            </div>

            <div style="
                color:#a7ffdf;
                font-size:34px;
                margin-top:25px;
            ">
                25°C
            </div>

            <div class="card-text">

                Live temperature indicator
                and smart hydration cues.

            </div>

        </div>
        """)


# ============================================================
# FEATURES
# ============================================================

def features_page():

    html("""
    <div class="section">

        <div class="eyebrow">
            AERIS TECHNOLOGY
        </div>

        <div class="title">
            Smart details. Simple experience.
        </div>

        <div class="text">

            Everything about AERIS is designed
            to make hydration simpler without
            adding unnecessary complexity.

        </div>

    </div>
    """)


    image_col, feature_col = st.columns(
        [1.1, 1],
        gap="large"
    )


    with image_col:

        st.image(
            image_path("6.jpeg"),
            use_container_width=True
        )


    with feature_col:

        features = [

            (
                "01",
                "Temperature Indicator",
                "A clear temperature readout gives you an at-a-glance view of your drink."
            ),

            (
                "02",
                "Smart Cap",
                "One-touch opening with a leak-resistant everyday design."
            ),

            (
                "03",
                "Hydration Reminder",
                "A subtle LED cue helps make drinking water part of your routine."
            ),

            (
                "04",
                "Insulated Body",
                "Designed to retain temperature while staying comfortable to carry."
            ),

        ]


        for number, title, description in features:

            html(f"""
            <div class="card" style="margin-bottom:15px;">

                <div style="
                    color:#a7ffdf;
                    font-size:30px;
                ">
                    {number}
                </div>

                <div class="card-title">
                    {title}
                </div>

                <div class="card-text">
                    {description}
                </div>

            </div>
            """)


    st.image(
        image_path("7.jpeg"),
        use_container_width=True
    )


# ============================================================
# ABOUT
# ============================================================

def about():

    image_col, text_col = st.columns(
        2,
        gap="large"
    )


    with image_col:

        st.image(
            image_path("5.jpeg"),
            use_container_width=True
        )


    with text_col:

        html("""
        <div class="section">

            <div class="eyebrow">
                OUR STORY
            </div>

            <div class="title">
                Small habits.<br>
                Big changes.
            </div>

            <div class="text">

                AERIS is built around a simple idea:
                better hydration should fit naturally
                into modern life.

            </div>

            <br>

            <div class="text">

                The product combines a reusable bottle
                with smart cues and a clean,
                lifestyle-first design.

            </div>

        </div>
        """)


    html("""
    <div class="light-section">

        <div class="eyebrow">
            OUR POSITIONING
        </div>

        <div class="title">
            Health. Design. Sustainability.
        </div>

    </div>
    """)


    values = [

        (
            "Health",
            "Encourages consistent hydration and makes the habit more visible."
        ),

        (
            "Design",
            "A minimal premium form designed for modern routines."
        ),

        (
            "Sustainability",
            "A reusable alternative to single-use plastic bottles."
        ),

    ]


    cols = st.columns(3)


    for col, (title, description) in zip(
        cols,
        values
    ):

        with col:

            html(f"""
            <div class="segment">

                <div class="segment-title">
                    {title}
                </div>

                <div class="segment-text">
                    {description}
                </div>

            </div>
            """)


# ============================================================
# CONTACT
# ============================================================

def contact():

    html("""
    <div class="section">

        <div class="eyebrow">
            GET IN TOUCH
        </div>

        <div class="title">
            Contact AERIS
        </div>

    </div>
    """)


    form_col, info_col = st.columns(
        2,
        gap="large"
    )


    with form_col:

        name = st.text_input("Name")

        email = st.text_input("Email")

        message = st.text_area(
            "Message",
            height=160
        )


        if st.button(
            "Send Message",
            use_container_width=True
        ):

            if (
                name.strip()
                and email.strip()
                and message.strip()
            ):

                st.success(
                    "Thanks! Your message has been received."
                )

            else:

                st.warning(
                    "Please complete all fields."
                )


    with info_col:

        html("""
        <div class="card">

            <div class="eyebrow">
                AERIS SUPPORT
            </div>

            <div class="card-title">
                Questions about the bottle?
            </div>

            <div class="card-text">

                Email: hello@aeris.example

                <br><br>

                Hours:
                Monday–Saturday,
                10:00–18:00

            </div>

        </div>
        """)


# ============================================================
# ROUTING
# ============================================================

if st.session_state.page == "Home":

    home()

elif st.session_state.page == "Shop":

    shop()

elif st.session_state.page == "Features":

    features_page()

elif st.session_state.page == "About":

    about()

elif st.session_state.page == "Contact":

    contact()


# ============================================================
# FOOTER
# ============================================================

html("""
<div class="footer">

    <span class="footer-logo">
        AERIS
    </span>

    <span style="margin-left:25px;">
        Drink Smart. Live Better.
    </span>

    <span style="float:right;">
        © 2025 AERIS. All rights reserved.
    </span>

</div>
""")
