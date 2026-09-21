import streamlit as st
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AERIS — Smart Hydration",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# IMAGE PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent


def image_path(filename):
    return str(BASE_DIR / filename)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "cart" not in st.session_state:
    st.session_state.cart = 0

if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

if "order_placed" not in st.session_state:
    st.session_state.order_placed = False


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       GLOBAL
       ================================ */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                #19383d 0%,
                #0c1b20 45%,
                #071217 100%
            );
        color: white;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* Hide Streamlit default elements */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* ================================
       BUTTONS
       ================================ */

    .stButton > button {
        border-radius: 30px;
        border: 1px solid #6e9d9d;
        background: transparent;
        color: white;
        height: 42px;
        transition: 0.25s ease;
    }

    .stButton > button:hover {
        border-color: #b7dddd;
        background: rgba(130, 190, 190, 0.10);
        color: white;
    }

    /* Primary button */

    .stButton > button[kind="primary"] {
        background: #8fbebe;
        border: none;
        color: #071217;
        font-weight: 600;
    }

    .stButton > button[kind="primary"]:hover {
        background: #b0d6d6;
        color: #071217;
    }

    /* ================================
       INPUTS
       ================================ */

    .stTextInput input,
    .stTextArea textarea {
        background: #101f24 !important;
        border: 1px solid #345158 !important;
        color: white !important;
        border-radius: 9px !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #8fbebe !important;
        box-shadow: none !important;
    }

    .stSelectbox > div > div,
    .stNumberInput > div > div {
        background: #101f24 !important;
        border-color: #345158 !important;
        color: white !important;
    }

    label {
        color: #a8bab9 !important;
    }

    /* ================================
       NAVBAR
       ================================ */

    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 0 25px 0;
        border-bottom: 1px solid rgba(140, 180, 180, 0.15);
        margin-bottom: 35px;
    }

    .logo {
        font-size: 24px;
        font-weight: 500;
        letter-spacing: 5px;
        color: white;
    }

    .logo-sub {
        font-size: 9px;
        letter-spacing: 3px;
        color: #8fa39f;
        margin-top: 3px;
    }

    /* ================================
       HERO
       ================================ */

    .hero-small {
        color: #8fa39f;
        font-size: 11px;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    .hero-title {
        font-size: clamp(45px, 6vw, 82px);
        line-height: 0.95;
        font-weight: 300;
        letter-spacing: -3px;
        color: white;
        margin-bottom: 25px;
    }

    .hero-text {
        color: #a9bcbb;
        font-size: 16px;
        line-height: 1.8;
        max-width: 560px;
    }

    /* ================================
       PRODUCT CARD
       ================================ */

    .product-card {
        background: rgba(20, 43, 48, 0.75);
        border: 1px solid #304b50;
        border-radius: 18px;
        padding: 25px;
    }

    .product-label {
        color: #8fa39f;
        font-size: 10px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .product-name {
        color: white;
        font-size: 31px;
        margin-top: 5px;
    }

    .product-description {
        color: #9fb1b0;
        font-size: 14px;
        line-height: 1.7;
        margin-top: 12px;
    }

    .price {
        color: white;
        font-size: 27px;
        font-weight: 500;
    }

    /* ================================
       INFO CARDS
       ================================ */

    .info-card {
        background: rgba(16, 39, 44, 0.65);
        border: 1px solid #29464b;
        border-radius: 15px;
        padding: 22px;
        height: 100%;
    }

    .info-number {
        font-size: 30px;
        color: white;
        margin-bottom: 5px;
    }

    .info-title {
        color: #8fa39f;
        font-size: 10px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* ================================
       FEATURE CARDS
       ================================ */

    .feature-card {
        background: rgba(16, 39, 44, 0.65);
        border: 1px solid #29464b;
        border-radius: 16px;
        padding: 25px;
        min-height: 190px;
    }

    .feature-icon {
        font-size: 28px;
        margin-bottom: 15px;
    }

    .feature-title {
        color: white;
        font-size: 18px;
        margin-bottom: 10px;
    }

    .feature-text {
        color: #91a6a5;
        font-size: 13px;
        line-height: 1.7;
    }

    /* ================================
       SECTION HEADINGS
       ================================ */

    .section-label {
        color: #8fa39f;
        font-size: 10px;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .section-title {
        color: white;
        font-size: 38px;
        font-weight: 300;
        margin-bottom: 15px;
    }

    /* ================================
       FOOTER
       ================================ */

    .footer {
        border-top: 1px solid rgba(140, 180, 180, 0.15);
        margin-top: 70px;
        padding-top: 25px;
        color: #718785;
        font-size: 12px;
        text-align: center;
    }

    /* ================================
       CART SUMMARY
       ================================ */

    .cart-summary {
        background: #102b30;
        border: 1px solid #29484d;
        border-radius: 14px;
        padding: 18px;
    }

    .cart-product-name {
        color: white;
        font-size: 17px;
    }

    .cart-product-sub {
        color: #8fa39f;
        font-size: 12px;
        margin-top: 4px;
    }

    /* ================================
       DIALOG
       ================================ */

    [data-testid="stDialog"] {
        background: #0b1b20 !important;
    }

    [data-testid="stDialog"] > div {
        background: #0b1b20 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

nav = st.columns([2.5, 1, 1, 1, 1, 1, 0.8])

with nav[0]:
    st.markdown(
        """
        <div class="logo">AERIS</div>
        <div class="logo-sub">SMART HYDRATION</div>
        """,
        unsafe_allow_html=True
    )

with nav[1]:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

with nav[2]:
    if st.button("Shop", use_container_width=True):
        st.session_state.page = "Shop"
        st.rerun()

with nav[3]:
    if st.button("Features", use_container_width=True):
        st.session_state.page = "Features"
        st.rerun()

with nav[4]:
    if st.button("About", use_container_width=True):
        st.session_state.page = "About"
        st.rerun()

with nav[5]:
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()

with nav[6]:
    if st.button(
        f"🛒 {st.session_state.cart}",
        key="cart_icon",
        use_container_width=True
    ):
        if st.session_state.cart > 0:
            st.session_state.show_cart = True
            st.rerun()
        else:
            st.info("Your cart is empty.")


# =========================================================
# CHECKOUT DIALOG
# =========================================================

@st.dialog("AERIS CHECKOUT")
def checkout_dialog():

    # =====================================================
    # ORDER SUCCESS
    # =====================================================

    if st.session_state.order_placed:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:25px 10px;
            ">

                <div style="
                    font-size:55px;
                    margin-bottom:10px;
                ">
                    ✓
                </div>

                <div style="
                    color:white;
                    font-size:26px;
                    font-weight:600;
                    margin-bottom:8px;
                ">
                    Order Confirmed
                </div>

                <div style="
                    color:#8fa39f;
                    font-size:14px;
                    line-height:1.6;
                ">
                    Thank you for choosing AERIS.<br>
                    Your AERIS One order has been placed successfully.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        total = 2499 * st.session_state.cart

        st.markdown(
            f"""
            <div style="
                background:#102b30;
                border:1px solid #28484d;
                border-radius:12px;
                padding:18px;
                margin-top:10px;
            ">

                <div style="
                    color:#8fa39f;
                    font-size:11px;
                    letter-spacing:2px;
                    text-transform:uppercase;
                ">
                    Order Summary
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    margin-top:14px;
                ">

                    <div>

                        <div style="
                            color:white;
                            font-size:17px;
                        ">
                            AERIS One
                        </div>

                        <div style="
                            color:#8fa39f;
                            font-size:12px;
                            margin-top:4px;
                        ">
                            ₹2,499 × {st.session_state.cart}
                        </div>

                    </div>

                    <div style="
                        color:white;
                        font-size:18px;
                        font-weight:600;
                    ">
                        ₹{total:,}
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "Close",
            use_container_width=True
        ):
            st.session_state.show_cart = False
            st.session_state.order_placed = False
            st.session_state.cart = 0
            st.rerun()

        return


    # =====================================================
    # CHECKOUT HEADER
    # =====================================================

    st.markdown(
        """
        <div style="
            margin-bottom:20px;
        ">

            <div style="
                color:#8fa39f;
                font-size:11px;
                letter-spacing:3px;
                text-transform:uppercase;
            ">
                AERIS ONE
            </div>

            <div style="
                color:white;
                font-size:30px;
                margin-top:5px;
                font-weight:500;
            ">
                Complete your order
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # PRODUCT SUMMARY
    # =====================================================

    total = 2499 * st.session_state.cart

    st.markdown(
        f"""
        <div style="
            background:#102b30;
            border:1px solid #28484d;
            border-radius:14px;
            padding:18px;
            margin-bottom:20px;
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
            ">

                <div>

                    <div style="
                        color:white;
                        font-size:17px;
                        font-weight:500;
                    ">
                        AERIS One
                    </div>

                    <div style="
                        color:#8fa39f;
                        font-size:12px;
                        margin-top:4px;
                    ">
                        Quantity: {st.session_state.cart}
                    </div>

                </div>

                <div style="
                    color:white;
                    font-size:18px;
                    font-weight:600;
                ">
                    ₹{total:,}
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # DELIVERY DETAILS
    # =====================================================

    st.markdown(
        """
        <div style="
            color:#8fa39f;
            font-size:11px;
            letter-spacing:2px;
            text-transform:uppercase;
            margin-bottom:8px;
        ">
            Delivery Details
        </div>
        """,
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Full Name",
        placeholder="Enter your full name"
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="10-digit mobile number"
    )

    address = st.text_area(
        "Address",
        placeholder="House / Flat number, Street, Area",
        height=90
    )

    col1, col2 = st.columns(2)

    with col1:
        city = st.text_input(
            "City",
            placeholder="Mumbai"
        )

    with col2:
        state = st.text_input(
            "State",
            placeholder="Maharashtra"
        )

    pincode = st.text_input(
        "Pincode",
        placeholder="6-digit pincode"
    )


    # =====================================================
    # PAYMENT
    # =====================================================

    st.markdown(
        """
        <div style="
            color:#8fa39f;
            font-size:11px;
            letter-spacing:2px;
            text-transform:uppercase;
            margin-top:15px;
            margin-bottom:8px;
        ">
            Payment Method
        </div>
        """,
        unsafe_allow_html=True
    )

    payment = st.radio(
        "Choose payment method",
        [
            "Cash on Delivery",
            "UPI — Demo",
            "Credit / Debit Card — Demo"
        ],
        label_visibility="collapsed"
    )


    # =====================================================
    # TOTAL
    # =====================================================

    st.markdown(
        f"""
        <div style="
            border-top:1px solid #28484d;
            margin-top:20px;
            padding-top:18px;
            display:flex;
            justify-content:space-between;
        ">

            <div style="
                color:#8fa39f;
                font-size:14px;
            ">
                Total
            </div>

            <div style="
                color:white;
                font-size:22px;
                font-weight:600;
            ">
                ₹{total:,}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # PLACE ORDER
    # =====================================================

    st.write("")

    if st.button(
        "Place Demo Order →",
        use_container_width=True,
        type="primary"
    ):

        if not name.strip():
            st.error("Please enter your name.")

        elif not phone.isdigit() or len(phone) != 10:
            st.error("Please enter a valid 10-digit phone number.")

        elif not address.strip():
            st.error("Please enter your address.")

        elif not city.strip():
            st.error("Please enter your city.")

        elif not state.strip():
            st.error("Please enter your state.")

        elif not pincode.isdigit() or len(pincode) != 6:
            st.error("Please enter a valid 6-digit pincode.")

        else:
            st.session_state.order_placed = True
            st.rerun()


# =========================================================
# OPEN CART
# =========================================================

if st.session_state.show_cart:
    checkout_dialog()


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "Home":

    hero_left, hero_right = st.columns(
        [1.05, 0.95],
        gap="large"
    )

    with hero_left:

        st.markdown(
            """
            <div class="hero-small">
                The future of hydration
            </div>

            <div class="hero-title">
                Smart hydration.<br>
                Simplified.
            </div>

            <div class="hero-text">
                Meet AERIS One — a smart hydration companion
                designed to make every sip count. Intelligent
                reminders, temperature awareness and a refined
                everyday design, all in one bottle.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "Explore AERIS One →",
            key="hero_shop",
            type="primary"
        ):
            st.session_state.page = "Shop"
            st.rerun()

    with hero_right:

        st.image(
            image_path("3.jpeg"),
            use_container_width=True
        )


    # =====================================================
    # PRODUCT INFORMATION
    # =====================================================

    st.write("")
    st.write("")

    left, right = st.columns(
        [0.95, 1.05],
        gap="large"
    )

    with left:

        st.image(
            image_path("3.jpeg"),
            use_container_width=True
        )

    with right:

        st.markdown(
            """
            <div class="product-label">
                AERIS ONE • SMART HYDRATION
            </div>

            <div class="product-name">
                More than a bottle.
            </div>

            <div class="product-description">
                AERIS One is designed as your everyday smart
                hydration companion. Stay aware of your water,
                temperature and daily hydration habits without
                compromising on style.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        stat1, stat2, stat3, stat4 = st.columns(4)

        with stat1:
            st.markdown(
                """
                <div class="info-card">
                    <div class="info-number">25°C</div>
                    <div class="info-title">Temperature</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with stat2:
            st.markdown(
                """
                <div class="info-card">
                    <div class="info-number">SMART</div>
                    <div class="info-title">Technology</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with stat3:
            st.markdown(
                """
                <div class="info-card">
                    <div class="info-number">24H</div>
                    <div class="info-title">Insulation</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with stat4:
            st.markdown(
                """
                <div class="info-card">
                    <div class="info-number">01</div>
                    <div class="info-title">Bottle</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        st.markdown(
            """
            <div class="product-description">

            ✓ Smart Hydration Reminders<br><br>

            ✓ Live Temperature Display<br><br>

            ✓ Insulated Construction<br><br>

            ✓ Built for Everyday Life

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        price_col, button_col = st.columns(
            [1, 1]
        )

        with price_col:

            st.markdown(
                """
                <div class="price">
                    ₹2,499
                </div>

                <div style="
                    color:#8fa39f;
                    font-size:11px;
                    margin-top:3px;
                ">
                    AERIS One
                </div>
                """,
                unsafe_allow_html=True
            )

        with button_col:

            if st.button(
                "🛒 Add AERIS One to Cart",
                key="home_cart",
                use_container_width=True
            ):
                st.session_state.cart += 1
                st.success("AERIS One added to cart.")


    # =====================================================
    # LIFESTYLE
    # =====================================================

    st.write("")
    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="section-label">
            Designed for your day
        </div>

        <div class="section-title">
            Wherever life takes you.
        </div>
        """,
        unsafe_allow_html=True
    )

    life1, life2, life3, life4 = st.columns(4)

    lifestyle_data = [
        ("🎓", "COLLEGE", "Stay hydrated through long classes and busy schedules."),
        ("💼", "OFFICE", "A refined companion for your everyday workspace."),
        ("🏋️", "GYM", "Keep hydration close through every workout."),
        ("✈️", "TRAVEL", "Designed to move with you wherever you go.")
    ]

    for col, data in zip(
        [life1, life2, life3, life4],
        lifestyle_data
    ):

        with col:

            st.markdown(
                f"""
                <div class="feature-card">

                    <div class="feature-icon">
                        {data[0]}
                    </div>

                    <div class="feature-title">
                        {data[1]}
                    </div>

                    <div class="feature-text">
                        {data[2]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# SHOP PAGE
# =========================================================

elif st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="section-label">
            AERIS COLLECTION
        </div>

        <div class="section-title">
            Choose your AERIS.
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    with left:

        st.image(
            image_path("3.jpeg"),
            use_container_width=True
        )

    with right:

        st.markdown(
            """
            <div class="product-label">
                AERIS ONE
            </div>

            <div class="product-name">
                Smart Hydration Bottle
            </div>

            <div class="product-description">
                Intelligent hydration meets modern everyday
                design. Built for college, work, gym and travel.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            """
            <div class="price">
                ₹2,499
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        finish = st.selectbox(
            "Finish",
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
            value=1,
            step=1
        )

        st.write("")

        if st.button(
            "Add to Cart",
            key="shop_add",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.cart += quantity

            st.success(
                f"{quantity} × AERIS One added to cart."
            )

        st.write("")

        if st.session_state.cart > 0:

            if st.button(
                "Proceed to Checkout →",
                key="shop_checkout",
                use_container_width=True
            ):

                st.session_state.show_cart = True
                st.rerun()


# =========================================================
# FEATURES PAGE
# =========================================================

elif st.session_state.page == "Features":

    st.markdown(
        """
        <div class="section-label">
            Technology
        </div>

        <div class="section-title">
            Built around better hydration.
        </div>

        <div class="hero-text">
            AERIS One combines smart functionality with
            an understated everyday design.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    f1, f2 = st.columns(2)

    with f1:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    💧
                </div>

                <div class="feature-title">
                    Smart Hydration Reminders
                </div>

                <div class="feature-text">
                    Stay aware of your hydration throughout
                    the day with intelligent reminders.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with f2:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🌡️
                </div>

                <div class="feature-title">
                    Temperature Awareness
                </div>

                <div class="feature-text">
                    Keep track of your drink temperature
                    with integrated temperature information.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    f3, f4 = st.columns(2)

    with f3:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    ❄️
                </div>

                <div class="feature-title">
                    Insulated Design
                </div>

                <div class="feature-text">
                    Designed to help maintain your drink's
                    temperature throughout the day.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with f4:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    ♻️
                </div>

                <div class="feature-title">
                    Reusable
                </div>

                <div class="feature-text">
                    A reusable everyday bottle designed
                    for modern routines.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# ABOUT PAGE
# =========================================================

elif st.session_state.page == "About":

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    with left:

        st.markdown(
            """
            <div class="section-label">
                About AERIS
            </div>

            <div class="section-title">
                Hydration,
                reimagined.
            </div>

            <div class="hero-text">
                AERIS was created around a simple idea:
                hydration should fit naturally into modern life.

                <br><br>

                AERIS One brings together thoughtful design,
                smart technology and everyday usability in
                one minimal product.
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.image(
            image_path("5.jpeg"),
            use_container_width=True
        )


# =========================================================
# CONTACT PAGE
# =========================================================

elif st.session_state.page == "Contact":

    st.markdown(
        """
        <div class="section-label">
            Get in touch
        </div>

        <div class="section-title">
            Let's talk.
        </div>

        <div class="hero-text">
            Have a question about AERIS One?
            Send us a message.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Name",
            placeholder="Your name"
        )

        email = st.text_input(
            "Email",
            placeholder="you@example.com"
        )

    with col2:

        message = st.text_area(
            "Message",
            placeholder="How can we help?",
            height=125
        )

    st.write("")

    if st.button(
        "Send Message →",
        type="primary"
    ):

        if name and email and message:
            st.success(
                "Thank you! Your message has been received."
            )
        else:
            st.warning(
                "Please fill in all fields."
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        AERIS • SMART HYDRATION
        <br><br>
        Designed for better everyday hydration.
    </div>
    """,
    unsafe_allow_html=True
)
